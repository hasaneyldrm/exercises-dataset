import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const dataPath = path.resolve(__dirname, '..', 'data', 'exercises.json');

const exercises = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

const byBodyPart = exercises.reduce((counts, exercise) => {
  counts[exercise.body_part] = (counts[exercise.body_part] ?? 0) + 1;
  return counts;
}, {});

const bodyweight = exercises.filter((exercise) => exercise.equipment === 'body weight');

console.log(`Total exercises: ${exercises.length}`);
console.log(`Bodyweight exercises: ${bodyweight.length}`);
console.log('Exercises by body part:');

for (const [bodyPart, count] of Object.entries(byBodyPart).sort((a, b) => b[1] - a[1])) {
  console.log(`- ${bodyPart}: ${count}`);
}

console.log('\nFirst exercise media attribution:');
console.log(exercises[0].attribution);
