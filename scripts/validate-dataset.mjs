#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const dataPath = path.join(rootDir, 'data', 'exercises.json');
const imageDir = path.join(rootDir, 'images');
const videoDir = path.join(rootDir, 'videos');

const LANGUAGES = ['en', 'es', 'it', 'tr', 'ru', 'zh'];
const REQUIRED_FIELDS = [
  'id',
  'name',
  'category',
  'body_part',
  'equipment',
  'instructions',
  'instruction_steps',
  'muscle_group',
  'secondary_muscles',
  'target',
  'image',
  'gif_url',
  'media_id',
  'created_at',
  'attribution',
];
const EXPECTED_ATTRIBUTION = '\u00a9 Gym visual \u2014 https://gymvisual.com/';

const errors = [];
const warnings = [];
const stats = {
  missingRequiredFields: 0,
  missingLanguageInstructions: 0,
  duplicateIds: 0,
  duplicateNames: 0,
  missingMediaFiles: 0,
  orphanMediaFiles: 0,
};

function relative(filePath) {
  return path.relative(rootDir, filePath).replaceAll(path.sep, '/');
}

function readJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (error) {
    errors.push(`Could not parse ${relative(filePath)}: ${error.message}`);
    return null;
  }
}

function listFiles(dir, extension) {
  if (!fs.existsSync(dir)) {
    errors.push(`Missing directory: ${relative(dir)}`);
    return [];
  }

  return fs.readdirSync(dir)
    .filter((fileName) => fileName.endsWith(extension))
    .map((fileName) => path.posix.join(relative(dir), fileName));
}

function isNonEmptyString(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

function countDuplicates(values) {
  const counts = new Map();
  for (const value of values) counts.set(value, (counts.get(value) ?? 0) + 1);
  return [...counts.entries()].filter(([, count]) => count > 1);
}

function addMissingFieldError(record, field) {
  stats.missingRequiredFields += 1;
  errors.push(`Record ${record.id ?? '<unknown>'} is missing required field "${field}"`);
}

function validateLanguageMaps(record) {
  for (const lang of LANGUAGES) {
    if (!isNonEmptyString(record.instructions?.[lang])) {
      stats.missingLanguageInstructions += 1;
      errors.push(`Record ${record.id} is missing instructions.${lang}`);
    }

    const steps = record.instruction_steps?.[lang];
    if (!Array.isArray(steps) || steps.length === 0 || steps.some((step) => !isNonEmptyString(step))) {
      stats.missingLanguageInstructions += 1;
      errors.push(`Record ${record.id} is missing valid instruction_steps.${lang}`);
    }
  }
}

function validateRecord(record, index) {
  if (typeof record !== 'object' || record === null || Array.isArray(record)) {
    errors.push(`Entry at index ${index} is not an object`);
    return;
  }

  for (const field of REQUIRED_FIELDS) {
    if (!(field in record) || record[field] === null || record[field] === '') {
      addMissingFieldError(record, field);
    }
  }

  if (!/^\d{4}$/.test(record.id ?? '')) {
    errors.push(`Record ${record.id ?? `<index ${index}>`} has invalid id format`);
  }

  for (const field of ['name', 'category', 'body_part', 'equipment', 'muscle_group', 'target', 'media_id']) {
    if (!isNonEmptyString(record[field])) {
      errors.push(`Record ${record.id ?? `<index ${index}>`} has invalid ${field}`);
    }
  }

  if (!Array.isArray(record.secondary_muscles) || record.secondary_muscles.some((muscle) => !isNonEmptyString(muscle))) {
    errors.push(`Record ${record.id} has invalid secondary_muscles`);
  }

  validateLanguageMaps(record);

  const expectedImage = `images/${record.id}-${record.media_id}.jpg`;
  const expectedGif = `videos/${record.id}-${record.media_id}.gif`;

  if (record.image !== expectedImage) {
    errors.push(`Record ${record.id} image should be "${expectedImage}", got "${record.image}"`);
  }

  if (record.gif_url !== expectedGif) {
    errors.push(`Record ${record.id} gif_url should be "${expectedGif}", got "${record.gif_url}"`);
  }

  if (record.attribution !== EXPECTED_ATTRIBUTION) {
    errors.push(`Record ${record.id} has invalid media attribution`);
  }

  if (!isNonEmptyString(record.created_at) || Number.isNaN(Date.parse(record.created_at))) {
    errors.push(`Record ${record.id} has invalid created_at timestamp`);
  }
}

function validateMediaReferences(records) {
  const imageRefs = new Set(records.map((record) => record.image).filter(Boolean));
  const gifRefs = new Set(records.map((record) => record.gif_url).filter(Boolean));
  const imageFiles = listFiles(imageDir, '.jpg');
  const gifFiles = listFiles(videoDir, '.gif');
  const imageFileSet = new Set(imageFiles);
  const gifFileSet = new Set(gifFiles);

  const missingImages = [...imageRefs].filter((filePath) => !imageFileSet.has(filePath));
  const missingGifs = [...gifRefs].filter((filePath) => !gifFileSet.has(filePath));
  const orphanImages = imageFiles.filter((filePath) => !imageRefs.has(filePath));
  const orphanGifs = gifFiles.filter((filePath) => !gifRefs.has(filePath));

  stats.missingMediaFiles = missingImages.length + missingGifs.length;
  stats.orphanMediaFiles = orphanImages.length + orphanGifs.length;

  for (const filePath of missingImages) errors.push(`Missing image file referenced by dataset: ${filePath}`);
  for (const filePath of missingGifs) errors.push(`Missing GIF file referenced by dataset: ${filePath}`);
  for (const filePath of orphanImages) errors.push(`Orphan image file not referenced by dataset: ${filePath}`);
  for (const filePath of orphanGifs) errors.push(`Orphan GIF file not referenced by dataset: ${filePath}`);

  return { imageFiles, gifFiles };
}

function main() {
  const records = readJson(dataPath);
  if (!records) return 1;

  if (!Array.isArray(records)) {
    errors.push('data/exercises.json must contain a JSON array');
    return 1;
  }

  records.forEach(validateRecord);

  const duplicateIds = countDuplicates(records.map((record) => record.id));
  const duplicateNames = countDuplicates(records.map((record) => record.name));
  stats.duplicateIds = duplicateIds.length;
  stats.duplicateNames = duplicateNames.length;

  for (const [id, count] of duplicateIds) {
    errors.push(`Duplicate id "${id}" appears ${count} times`);
  }

  for (const [name, count] of duplicateNames) {
    warnings.push(`Duplicate exercise name "${name}" appears ${count} times`);
  }

  const { imageFiles, gifFiles } = validateMediaReferences(records);

  console.log('Dataset validation');
  console.log(`Records: ${records.length}`);
  console.log(`Images: ${imageFiles.length}`);
  console.log(`GIFs: ${gifFiles.length}`);
  console.log(`Missing required fields: ${stats.missingRequiredFields}`);
  console.log(`Missing language instructions: ${stats.missingLanguageInstructions}`);
  console.log(`Duplicate IDs: ${stats.duplicateIds}`);
  console.log(`Missing media files: ${stats.missingMediaFiles}`);
  console.log(`Orphan media files: ${stats.orphanMediaFiles}`);
  console.log(`Duplicate-name warnings: ${stats.duplicateNames}`);
  console.log(`Warnings: ${warnings.length}`);

  if (errors.length > 0) {
    console.error('\nValidation failed:');
    for (const error of errors) console.error(`- ${error}`);
    return 1;
  }

  if (warnings.length > 0) {
    console.log('\nValidation warnings:');
    for (const warning of warnings) console.log(`- ${warning}`);
  }

  console.log('Validation passed');
  return 0;
}

process.exitCode = main();
