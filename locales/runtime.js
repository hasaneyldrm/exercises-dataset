(function (root) {
  'use strict';

  const STORAGE_KEY = 'exercises-language';
  const BASE_LOCALE = 'en';
  const registry = Object.create(null);
  const loading = Object.create(null);
  let currentLocale = BASE_LOCALE;

  function manifest() {
    return Array.isArray(root.EXERCISE_LOCALE_MANIFEST)
      ? root.EXERCISE_LOCALE_MANIFEST
      : [];
  }

  function localeEntry(code) {
    return manifest().find(entry => entry.code === code) || null;
  }

  function format(message, params) {
    if (typeof message !== 'string') return message;
    return message.replace(/\{([a-zA-Z0-9_]+)\}/g, (match, key) =>
      Object.prototype.hasOwnProperty.call(params || {}, key) ? String(params[key]) : match);
  }

  function readStoredLocale() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      return localeEntry(stored) ? stored : null;
    } catch (_) {
      return null;
    }
  }

  function browserLocales() {
    const values = Array.isArray(navigator.languages) && navigator.languages.length
      ? navigator.languages
      : [navigator.language];
    return values.filter(Boolean).map(value => String(value).toLowerCase());
  }

  function aliasMatches(language, alias) {
    const normalized = String(alias).toLowerCase();
    if (normalized.endsWith('-*')) {
      return language === normalized.slice(0, -2) || language.startsWith(normalized.slice(0, -1));
    }
    return language === normalized;
  }

  function resolveInitialLocale() {
    const stored = readStoredLocale();
    if (stored) return stored;

    for (const language of browserLocales()) {
      for (const entry of manifest()) {
        const aliases = Array.isArray(entry.browserLanguages) ? entry.browserLanguages : [entry.code];
        if (aliases.some(alias => aliasMatches(language, alias))) return entry.code;
      }
    }
    return BASE_LOCALE;
  }

  function registerLocale(pack) {
    if (!pack || typeof pack !== 'object' || !localeEntry(pack.code)) {
      throw new Error('Cannot register an unknown exercise locale.');
    }
    registry[pack.code] = Object.assign({
      dir: 'ltr',
      complete: false,
      isBase: false,
      ui: {},
      instructionLabels: {},
      taxonomy: {},
      records: {},
    }, pack);
    return registry[pack.code];
  }

  function loadLocale(code) {
    if (registry[code]) return Promise.resolve(registry[code]);
    if (loading[code]) return loading[code];

    const entry = localeEntry(code);
    if (!entry) return Promise.reject(new Error(`Unknown locale: ${code}`));

    loading[code] = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = entry.path;
      script.async = true;
      script.onload = () => {
        delete loading[code];
        if (registry[code]) resolve(registry[code]);
        else reject(new Error(`Locale did not register itself: ${code}`));
      };
      script.onerror = () => {
        delete loading[code];
        reject(new Error(`Could not load locale: ${code}`));
      };
      document.head.appendChild(script);
    });
    return loading[code];
  }

  function applyDocumentLocale(pack) {
    document.documentElement.lang = pack.code;
    document.documentElement.dir = pack.dir || 'ltr';
  }

  async function setLocale(code, options) {
    const settings = Object.assign({ persist: true, notify: true }, options);
    let pack;
    try {
      pack = await loadLocale(code);
    } catch (error) {
      if (code === BASE_LOCALE) throw error;
      pack = await loadLocale(BASE_LOCALE);
      code = BASE_LOCALE;
    }

    currentLocale = code;
    applyDocumentLocale(pack);
    if (settings.persist) {
      try { localStorage.setItem(STORAGE_KEY, code); } catch (_) { /* storage unavailable */ }
    }
    if (settings.notify) {
      root.dispatchEvent(new CustomEvent('exercises:localechange', { detail: { code, pack } }));
    }
    return pack;
  }

  async function init() {
    await loadLocale(BASE_LOCALE);
    return setLocale(resolveInitialLocale(), { persist: false, notify: false });
  }

  async function loadAllLocales() {
    const results = await Promise.all(manifest().map(entry => loadLocale(entry.code)));
    return results;
  }

  function getPack(code) {
    return registry[code || currentLocale] || null;
  }

  function valueFrom(pack, page, key) {
    return pack && pack.ui && pack.ui[page] ? pack.ui[page][key] : undefined;
  }

  function t(page, key, params) {
    const selected = valueFrom(getPack(), page, key);
    const fallback = valueFrom(getPack(BASE_LOCALE), page, key);
    return format(selected === undefined ? (fallback === undefined ? key : fallback) : selected, params || {});
  }

  function taxonomyValue(pack, group, value) {
    const map = pack && pack.taxonomy ? pack.taxonomy[group] : null;
    return map && Object.prototype.hasOwnProperty.call(map, value) ? map[value] : undefined;
  }

  function localizeField(record, field) {
    const pack = getPack();
    const translated = pack && pack.records ? pack.records[record.id] : null;
    if (field === 'name' && translated && translated.name) return translated.name;

    const groups = {
      category: 'categories',
      body_part: 'bodyParts',
      equipment: 'equipment',
      target: 'targets',
      muscle_group: 'muscles',
    };
    const localized = groups[field] ? taxonomyValue(pack, groups[field], record[field]) : undefined;
    return localized === undefined ? record[field] : localized;
  }

  function localizeArray(record, field) {
    const values = Array.isArray(record[field]) ? record[field] : [];
    if (field !== 'secondary_muscles') return values.slice();
    const pack = getPack();
    return values.map(value => taxonomyValue(pack, 'muscles', value) || value);
  }

  function packForInstructionCode(code) {
    if (!code) return getPack();
    const selected = getPack();
    if (selected && (selected.code === code || selected.instructionCode === code)) return selected;
    return Object.values(registry).find(pack => pack.code === code || pack.instructionCode === code) || null;
  }

  function getInstructionSteps(record, requestedCode) {
    const pack = packForInstructionCode(requestedCode);
    const translated = pack && pack.records ? pack.records[record.id] : null;
    if (translated && Array.isArray(translated.steps) && translated.steps.length) {
      return translated.steps.slice();
    }

    const code = requestedCode || (pack && pack.instructionCode) || BASE_LOCALE;
    if (record.instruction_steps && Array.isArray(record.instruction_steps[code])) {
      return record.instruction_steps[code].slice();
    }
    if (record.instructions && typeof record.instructions[code] === 'string') {
      return [record.instructions[code]];
    }
    if (record.instruction_steps && Array.isArray(record.instruction_steps.en)) {
      return record.instruction_steps.en.slice();
    }
    return record.instructions && record.instructions.en ? [record.instructions.en] : [];
  }

  function getInstructionLabel(code) {
    const selected = getPack();
    const fallback = getPack(BASE_LOCALE);
    return (selected && selected.instructionLabels && selected.instructionLabels[code])
      || (fallback && fallback.instructionLabels && fallback.instructionLabels[code])
      || code;
  }

  root.ExercisesI18n = {
    registerLocale,
    init,
    loadLocale,
    loadAllLocales,
    setLocale,
    getLocale: () => currentLocale,
    getPack,
    getAvailableLocales: () => manifest().map(entry => Object.assign({}, entry)),
    t,
    format,
    localizeField,
    localizeArray,
    getInstructionSteps,
    getInstructionLabel,
  };
})(window);
