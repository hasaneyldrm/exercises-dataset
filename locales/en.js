window.ExercisesI18n.registerLocale({
  code: 'en',
  label: 'English',
  instructionCode: 'en',
  dir: 'ltr',
  complete: true,
  isBase: true,
  ui: {
    index: {
      pageTitle: 'Exercise Library',
      languageLabel: 'Interface language',
      interfaceLanguage: 'Interface language',
      databaseSetup: 'Database Setup',
      databaseSetupShort: 'Database',
      searchPlaceholder: 'Search exercises, body parts, equipment, or muscles…',
      searchLabel: 'Search exercises',
      clearSearch: 'Clear search',
      category: 'Category',
      equipment: 'Equipment',
      targetMuscle: 'Target Muscle',
      loadingMore: 'Loading more exercises',
      close: 'Close',
      databaseSubtitle: 'Import 1,324 exercises into your database in 3 steps.',
      createTable: 'Create Table',
      createTableDescription: 'Run this in your database client (SSMS, DBeaver, pgAdmin, etc.):',
      copy: 'Copy',
      copied: 'Copied!',
      importData: 'Import Data',
      importDataDescription: 'Generate a <code>.sql</code> file for all 1,324 exercises and registered translations. The file is built entirely in your browser; nothing is uploaded.',
      generateInsertSql: 'Generate INSERT SQL',
      mediaFiles: 'Media Files',
      mediaFilesDescription: 'Copy the <code>images/</code> and <code>videos/</code> folders to your web server root or CDN. The <code>image</code> and <code>gif_url</code> columns store relative paths.',
      mediaLayout: 'your-server.com/\n├── images/   ← 1,324 JPG thumbnails\n└── videos/   ← 1,324 GIF animations',
      showMore: '+{count} more',
      noExercises: 'No exercises found',
      allExercises: '{count} exercises',
      filteredExercises: '{count} of {total} exercises',
      removeFilter: 'Remove {label} filter',
      clearAll: 'Clear all',
      openExercise: 'View {name} exercise details',
      exerciseImage: '{name} exercise demonstration',
      bodyPart: 'Body Part',
      target: 'Target',
      muscles: 'Muscles',
      primary: 'Primary',
      secondary: 'Secondary',
      instructions: 'Instructions',
      generating: 'Generating…',
      downloaded: '✓ Downloaded {file}',
      generateError: 'Error generating file.',
    },
    setup: {
      pageTitle: 'Developer Setup · ExerciseDB',
      headerLabel: 'Developer Setup',
      languageLabel: 'Interface language',
      languageSwitchLabel: 'Interface language',
      backBrowse: 'Back to Browse',
      contents: 'Contents',
      navDb: 'Database Setup',
      navApi: 'API Integration',
      navLlm: 'Ask Your LLM',
      dbTitle: 'Database Setup',
      dbDesc: 'Import all 1,324 exercises and registered translations into your database in 3 steps. Choose your database engine below.',
      dbTabsLabel: 'Database engine',
      createTitle: 'Create Tables',
      createDesc: 'Run this in your database client (SSMS, DBeaver, pgAdmin, TablePlus, etc.):',
      copy: 'Copy',
      copied: 'Copied!',
      copyFailed: 'Copy failed',
      copyCreateLabel: 'Copy CREATE TABLE SQL',
      importTitle: 'Import Data',
      importDesc: 'Generate a <code>.sql</code> file with all 1,324 exercises and every registered non-base locale. The file is built entirely in your browser; nothing is uploaded.',
      generate: 'Generate INSERT SQL',
      generateLabel: 'Generate and download INSERT SQL',
      loading: 'Loading exercise data…',
      loadingLocales: 'Loading translation packs…',
      generating: 'Generating…',
      downloaded: '✓ Downloaded {filename}',
      generateError: 'Error generating file.',
      fileProtocolError: 'SQL generation cannot read data from file://. Start a local server with “python3 -m http.server 8000”, then open http://localhost:8000/setup.html.',
      localeLoadError: 'Could not load all registered translation packs.',
      mediaTitle: 'Media Files',
      mediaDesc: 'Place the media folders in your web server root or CDN. The <code>image</code> and <code>gif_url</code> columns store relative paths; prepend your base URL in your app.',
      mediaTree: 'your-server.com/\n├── images/   ← 1,324 JPG thumbnails\n└── videos/   ← 1,324 GIF animations',
      mediaNote: 'The <code>images/</code> and <code>videos/</code> folders are included in the repository. Copy them to your server or CDN; no separate download is needed.',
      apiTitle: 'API Integration',
      apiDesc: 'Client-side examples showing how to call your backend API. Enter your API base URL below; all examples update live.',
      baseUrlLabel: 'API base URL',
      clientLanguageLabel: 'Client language',
      getOneDesc: 'Fetch a single exercise by ID',
      getAllDesc: 'Paginated list of exercises',
      getFilteredDesc: 'Filter by category, body part, equipment, and target muscle',
      copyCodeLabel: 'Copy code',
      llmTitle: 'Ask Your LLM',
      llmDesc: 'Copy this prompt into ChatGPT, Claude, Gemini, or another LLM to generate a complete backend with locale-aware exercise responses.',
      frameworkLabel: 'Framework',
      databaseLabel: 'Database',
      promptLabel: 'Backend API generation prompt',
      copyPrompt: 'Copy Prompt',
      copyPromptLabel: 'Copy prompt',
      llmHint: 'Paste into ChatGPT, Claude, Gemini, or another LLM',
      llmPrompt: `You are a senior {frameworkLanguage} developer. Build a complete REST API using {frameworkName} for an exercise/fitness database.

## Dataset Overview
- 1,324 fitness exercises
- The exercises table contains the canonical English fields and multilingual instruction columns.
- The exercise_translations table contains locale-specific names, taxonomy labels, muscles, instructions, and instruction step arrays. Its primary key is (exercise_id, locale).
- If a requested translation is missing, fall back to the canonical English exercise.

## Database Schema ({databaseName})
\`\`\`sql
{schema}
\`\`\`

## Required Endpoints

### 1. GET /exercises/:id
- Return a single exercise by id.
- Accept optional locale (BCP 47 code, for example zh-CN) and join exercise_translations when supplied.
- Return a 404 JSON error if the exercise is not found: { "error": "Exercise not found" }.

### 2. GET /exercises
Optional query parameters:
- page (integer, default 1)
- limit (integer, default 20, maximum 100)
- category, body_part, equipment, muscle_group, target (case-insensitive partial matches)
- locale (BCP 47 code; fall back to English when a translation is unavailable)

Return data, total, page, limit, and totalPages.

### 3. GET /exercises/random
- Return one random, optionally localized exercise.

### 4. GET /categories
### 5. GET /body-parts
### 6. GET /equipment
- Return sorted, unique values and honor the optional locale parameter.

## Technical Requirements
- Read the database connection string from an environment variable.
- Use parameterized queries; never interpolate user input into SQL.
- Return JSON with Content-Type: application/json.
- Enable configurable CORS.
- Validate page and limit, return 400 for invalid values, and return 500 for unexpected errors.
- Log method, path, status code, and duration for each request.

## Packages
{packages}

## Deliverables
1. Complete, runnable source code with every required file.
2. Setup instructions for installing dependencies and running \`{runCommand}\`.

Write production-quality code and do not omit error handling.`,
    },
  },
  instructionLabels: {
    en: 'English',
    es: 'Spanish',
    it: 'Italian',
    tr: 'Turkish',
    ru: 'Russian',
    zh: 'Simplified Chinese',
    hi: 'Hindi',
    pl: 'Polish',
    ko: 'Korean',
  },
  taxonomy: {
    categories: {},
    bodyParts: {},
    equipment: {},
    targets: {},
    muscles: {},
  },
  records: {},
});
