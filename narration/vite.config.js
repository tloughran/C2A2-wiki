import { defineConfig } from 'vite';

export default defineConfig({
  // Use relative asset URLs so the built bundle works when opened as file://
  // as well as when served from any static host.
  base: './',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    // Single HTML deliverable for easy distribution; data/ stays as external JSON
    rollupOptions: {
      output: {
        manualChunks: undefined
      }
    }
  },
  server: {
    port: 5173,
    open: false
  }
});
