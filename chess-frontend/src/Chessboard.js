import React, { useState } from 'react';
import { Chessboard } from 'react-chessboard';

const ChessGame = () => {
  const [boardPosition, setBoardPosition] = useState(null);

  const handlePieceMove = (move) => {
    console.log("Move:", move);
    setBoardPosition(move);
  };

  return (
    <div>
      <Chessboard
        boardPosition={boardPosition}  // pass current board position
        onPieceMove={handlePieceMove}   // handle piece movement
      />
    </div>
  );
};

export default ChessGame;
