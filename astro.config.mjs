import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://laoli-notes.vercel.app',
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
    },
  },
});
