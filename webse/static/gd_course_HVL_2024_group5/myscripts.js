const dot = document.querySelector('.animated-dot');

let mouseX = 0;
let mouseY = 0;

let ballX = 0;
let ballY = 0;

let speed = 0.2;  // how fast the dot catches up to the mouse pointer;

function animate() {
  let distX = mouseX - ballX;
  let distY = mouseY - ballY;
      
  ballX = ballX + (distX * speed);
  ballY = ballY + (distY * speed);
  
  dot.style.left = ballX + 'px';
  dot.style.top = ballY + 'px';

  requestAnimationFrame(animate);
}

animate();

dot.addEventListener('mouseenter', function() {
  dot.classList.add('active');
});

dot.addEventListener('mouseleave', function() {
  dot.classList.remove('active');
});

document.addEventListener('mousemove', function(e){
  mouseX = e.pageX;
  mouseY = e.pageY;
});

document.addEventListener('click', function(){
  dot.classList.remove('active');
  // Trigger reflow
  void dot.offsetWidth;
  dot.classList.add('active');
}, false);
