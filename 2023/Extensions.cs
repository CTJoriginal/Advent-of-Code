using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC_2023
{
    public static class Extensions
    {
        public static int[,] Transpose(this int[,] matrix)
        {
            int x = matrix.GetLength(0), y = matrix.GetLength(1);
        
            int[,] trans = new int[y, x];

            for (int collumn = 0; collumn < x; collumn++) // Move from left to right
            { 
                for (int row = 0; row < y; row++) // Move from north to south
                {
                    trans[collumn, row] = matrix[row, collumn];
                }
            }

            return trans;
        }
        public static int[,] Rotate(this int[,] oldMatrix) //CW
        {
            int x = oldMatrix.GetLength(0), y = oldMatrix.GetLength(1);
            int[,] rotatedMatrix = new int[y, x];

            for (int row = 0; row < y; row++) // Move from north to south
            {
                for (int column = 0; column < x; column++) // Move from left to right
                {
                    rotatedMatrix[row, column] = oldMatrix[x - column - 1, row];
                }
            }

            return rotatedMatrix;
        }

    }
}
