import { defineConfig, presetWind3 } from 'unocss';

// Tailwind-compatible utilities for our TSX and MDX, not Fumadocs internals.
export default defineConfig({
  presets: [presetWind3()],
  content: { filesystem: ['app/**/*.{ts,tsx}', 'content/docs/**/*.mdx'] },
  shortcuts: {
    'field-hero-grid': 'grid items-center gap-[5vw] grid-cols-1 min-[741px]:grid-cols-[1.25fr_1fr]',
    'field-entry-grid': 'grid gap-4 grid-cols-1 min-[741px]:grid-cols-3',
  },
});
