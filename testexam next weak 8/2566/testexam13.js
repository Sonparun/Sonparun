//A large flat field measures 50x50 kilometers,At atime t=0 a bomb explodes somewhere on the field.There are 3 scattered sensors with synchrinized clocks that record the exact time (in seconds) that the sound of the exploding bomb reaches them.
//Given the x,y coordinates of each of the 3 sensors abd the recorded time of each, find the location of the bomb:
//bomb([[x1,y1,t1],[x2,y2,t2],[x3,y3,t3]]) -> [xb,yb]
//Bomb location

//Example
//bomb([[0,0,72.886],[0,50,72.886],[25,25,72.886]]) -> [0,25]
//bomb([[0,50,145.773],[50,50,206.154],[50,0,145.773]]) -> [0,0]
//bomb([[5,8,48.872],[12,21,35.107],[24,20,22.203]]) -> [21,13]
//bomb([[18,42,35.558],[39,16,106.004],[7,24,32.202]]) -> [8,35]
  
function bomb(sensors) {
    const [x1, y1, t1] = sensors[0];
    const [x2, y2, t2] = sensors[1];
    const [x3, y3, t3] = sensors[2];
  
    const A = 2 * x2 - 2 * x1;
    const B = 2 * y2 - 2 * y1;
    const C = (t1 * t1) - (t2 * t2) - (x1 * x1) + (x2 * x2) - (y1 * y1) + (y2 * y2);
  
    const D = 2 * x3 - 2 * x1;
    const E = 2 * y3 - 2 * y1;
    const F = (t1 * t1) - (t3 * t3) - (x1 * x1) + (x3 * x3) - (y1 * y1) + (y3 * y3);
  
    const xb = (C * E - F * B) / (E * A - B * D);
    const yb = (C * D - A * F) / (B * D - A * E);
  
    return [xb, yb];
  }
  
  console.log(bomb([[0, 0, 72.886], [0, 50, 72.886], [25, 25, 72.886]])); // Output: [0, 25]
  console.log(bomb([[0, 50, 145.773], [50, 50, 206.154], [50, 0, 145.773]])); // Output: [0, 0]
  console.log(bomb([[5, 8, 48.872], [12, 21, 35.107], [24, 20, 22.203]])); // Output: [21, 13]
  console.log(bomb([[18, 42, 35.558], [39, 16, 106.004], [7, 24, 32.202]])); // Output: [8, 35]
  
  