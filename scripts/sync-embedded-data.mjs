import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(scriptDir, '..');
const dataPath = path.join(rootDir, 'data', 'exercises.json');
const indexPath = path.join(rootDir, 'index.html');
const setupPath = path.join(rootDir, 'setup.html');

const exercises = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
if (!Array.isArray(exercises) || exercises.length !== 1324) {
  throw new Error(`数据记录数异常：${exercises.length}`);
}

function replaceIndexData(source) {
  const marker = '  const EXERCISES = ';
  const start = source.indexOf(marker);
  if (start === -1) throw new Error('index.html 中未找到 EXERCISES 数据标记');

  const valueStart = start + marker.length;
  const end = source.indexOf(';\n', valueStart);
  if (end === -1) throw new Error('index.html 中未找到 EXERCISES 数据结尾');

  return `${source.slice(0, valueStart)}${JSON.stringify(exercises)}${source.slice(end)}`;
}

function replaceSetupData(source) {
  const marker = '<script type="application/json" id="exercise-data">';
  const start = source.indexOf(marker);
  if (start === -1) throw new Error('setup.html 中未找到 exercise-data 数据标记');

  const valueStart = start + marker.length;
  const end = source.indexOf('</script>', valueStart);
  if (end === -1) throw new Error('setup.html 中未找到 exercise-data 数据结尾');

  const prettyJson = JSON.stringify(exercises, null, 2);
  return `${source.slice(0, valueStart)}${prettyJson}${source.slice(end)}`;
}

function writeIfChanged(filePath, nextContent) {
  const currentContent = fs.readFileSync(filePath, 'utf8');
  if (currentContent === nextContent) return false;
  fs.writeFileSync(filePath, nextContent, 'utf8');
  return true;
}

const indexSource = fs.readFileSync(indexPath, 'utf8');
const setupSource = fs.readFileSync(setupPath, 'utf8');
const indexChanged = writeIfChanged(indexPath, replaceIndexData(indexSource));
const setupChanged = writeIfChanged(setupPath, replaceSetupData(setupSource));

console.log(`index.html：${indexChanged ? '已同步' : '无需更新'}`);
console.log(`setup.html：${setupChanged ? '已同步' : '无需更新'}`);
