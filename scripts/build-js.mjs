import { readFile, writeFile } from 'node:fs/promises';

// Keep the upstream Academic Pages script order. No npm dependencies are needed.
const root = new URL('../', import.meta.url);
const sources = [
  'assets/js/plugins/jquery.greedy-navigation.js',
  'assets/js/_main.js',
  'assets/js/theme.js',
];
const parts = await Promise.all(sources.map(path => readFile(new URL(path, root), 'utf8')));
await writeFile(new URL('assets/js/site.js', root), parts.join('\n;\n'), 'utf8');
console.log('Built assets/js/site.js from the Academic Pages scripts.');
