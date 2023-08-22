//Create a function that the name of a chess piece, its position and a target position, The function should return true if the piece can move to the target and false if it can't
//The possible inputs are"Pawn","Knight","Bishop","Rook","Queen"and"King".

//canMove("Rook","A8","H8") -> true
//canMove("Bishop","A7","G1") -> true
//canMove("Queen","C4","D6") -> false

function canMove(piece, start, target) {
    const startFile = start.charCodeAt(0) - 65;
    const startRank = parseInt(start[1], 10) - 1;
    
    const targetFile = target.charCodeAt(0) - 65;
    const targetRank = parseInt(target[1], 10) - 1;
    
    const fileDifference = Math.abs(targetFile - startFile);
    const rankDifference = Math.abs(targetRank - startRank);
    
    switch (piece) {
      case "Pawn":
        return startFile === targetFile && (startRank === targetRank - 1);
      case "Knight":
        return (fileDifference === 2 && rankDifference === 1) || (fileDifference === 1 && rankDifference === 2);
      case "Bishop":
        return fileDifference === rankDifference;
      case "Rook":
        return startFile === targetFile || startRank === targetRank;
      case "Queen":
        return startFile === targetFile || startRank === targetRank || fileDifference === rankDifference;
      case "King":
        return fileDifference <= 1 && rankDifference <= 1;
      default:
        return false;
    }
  }
  console.log(canMove("Pawn", "C3", "C2")); // Output: true
  console.log(canMove("Rook", "A8", "H8")); // Output: true
  console.log(canMove("Bishop", "A7", "G1")); // Output: true
  console.log(canMove("Queen", "C4", "D6")); // Output: false
  