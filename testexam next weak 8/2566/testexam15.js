//A frog wants ti cross a river.Unfortuneately,he can't jump across in a single leap.Luckyily,there are n stones in river.
//The frog can jump from the near bank to stone 1 and from stone n to the far bank. He can also jump from stone to stone,forward and baclward.However,on each stone, a number j is written and he must only jump exactly j stones backward or forward.
//Return the minimum number of jumps to cross the river (including jumps to the first stone and from the last stone(orany other stone,ifpossuble)to the far bank)or no chance :-( if it's not possible to cross the river.
//Example
//jumpingFrog(5,[1,1,1,1,1]) -> 6
//jumpingFrog(5,[1,3,1,1,1]) -> 4
//jumpingFrog(5,[1,1,0,1,1]) -> "no chance :-("