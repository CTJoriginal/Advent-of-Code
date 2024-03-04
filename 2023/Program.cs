using System.Diagnostics;
using System.IO;

namespace AdventOfCode
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();

            try
            {
                Days.Day13();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                Console.WriteLine(ex.StackTrace);
            }

            sw.Stop();
            Console.WriteLine();
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine(sw.ElapsedMilliseconds > 1000 ? sw.ElapsedMilliseconds / 1000 + " s" : sw.ElapsedMilliseconds + " ms");
            Console.ResetColor();
        }
    }

    public static class Functions
    {
        public static string[] GetInput(int InputNumber)
        {
            return File.ReadAllLines($"Inputs/{InputNumber}.txt");
        }

        public static string GetInputAllText(int InputNumber)
        {
            return File.ReadAllText($"Inputs/{InputNumber}.txt");
        }
    } 
}