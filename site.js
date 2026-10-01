const control = document.querySelector('.motion-toggle');
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
function setPaused(paused) {
  document.body.classList.toggle('motion-paused', paused);
  control.setAttribute('aria-pressed', String(paused));
  control.textContent = paused ? 'Bewegung aktivieren' : 'Bewegung pausieren';
}
setPaused(reduced.matches);
control.addEventListener('click', () => setPaused(!document.body.classList.contains('motion-paused')));
reduced.addEventListener('change', event => setPaused(event.matches));
