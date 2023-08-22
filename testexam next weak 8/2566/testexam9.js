//Write a function that takes the number of seconds and returns the digital format clock time as a string. Time dhould be counted from 00:00:00

//digitalClock(5925) -> "01:23:45"
// 5025 seconds is 1 hour, 23 mins, 45 secs.

//digitalClock(61201) -> "17:00:01"
// No AM/PM. 24j format.

//digitalClock(87000) -> "00:10:00"
// IT's 00:10 next day

function digitalClock(seconds) {
    const h = (seconds / 3600 | 0) % 24;
    const m = (seconds / 60 | 0) % 60;
    const s = seconds % 60;
    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`; }
  
  console.log(digitalClock(5925));
  console.log(digitalClock(61201));
  console.log(digitalClock(87000));
  console.log(digitalClock(4200));
  console.log(digitalClock(48795));
  
  