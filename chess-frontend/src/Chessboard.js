import React, { useState } from 'react';
import { Chessboard } from 'react-chessboard';

const ChessBoardUI = () => {
  const [boardPosition, setBoardPosition] = useState('start'); // Starting position

  const handleMove = (from, to) => {
    console.log(`Move from ${from} to ${to}`);
    // update the board position or communicate with the backend here later
  };

  return (
    <div>
      <Chessboard position={boardPosition} onPieceDrop={handleMove} />
    </div>
  );
};

export default ChessBoardUI;
