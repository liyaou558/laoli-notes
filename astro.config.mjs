import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://liyaou558.github.io',
  base: '/laoli-notes/',
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
    },
  },
});
