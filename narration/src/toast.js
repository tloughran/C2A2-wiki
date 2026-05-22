// Minimal toast notifier. Surfaces errors (especially TTS) so they don't die
// silently in the console. One of the root causes of our earlier debugging
// pain was that speakWithAPI fallback happened without the user knowing.

const container = () => document.getElementById('toast-container');

export function toast(message, { type = 'info', duration = 4000 } = {}) {
  const el = document.createElement('div');
  el.className = `toast toast--${type}`;
  el.textContent = message;
  container().appendChild(el);
  requestAnimationFrame(() => el.classList.add('visible'));
  setTimeout(() => {
    el.classList.remove('visible');
    setTimeout(() => el.remove(), 300);
  }, duration);
}

export const info = (msg) => toast(msg, { type: 'info' });
export const success = (msg) => toast(msg, { type: 'success' });
export const warn = (msg) => toast(msg, { type: 'warn' });
export const error = (msg) => toast(msg, { type: 'error', duration: 7000 });
