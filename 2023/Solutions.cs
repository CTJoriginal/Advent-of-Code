using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

using AdventOfCode;
using Microsoft.Recognizers.Text.InternalCache;
using System.Runtime.InteropServices;
using Microsoft.Recognizers.Text.Matcher;
using System.Security.Cryptography;
using System.Runtime.ExceptionServices;
using System.Diagnostics;
using System.ComponentModel.Design;
using Microsoft.Recognizers.Definitions;
using System.Data;
using AoC_2023;

public static class Days
{
    public static void Day1()
    {
        //Part 1
        var input = Functions.GetInput(1);
        List<int> Codes = [];
        foreach (string item in input)
        {
            var CharCode = item.Where(char.IsDigit).ToList(); // Select characters that are digits

            //Codes.Add(int.Parse($"{CharCode.First()}{CharCode.Last()}"));
        }

        Console.WriteLine("Part 1: " + Codes.Sum());

        //Part 2
        Codes = [];

        foreach (string item in input)
        {

            //var CharCode = Numbered.Where(char.IsDigit).ToList(); // Select characters that are digits

            //Console.WriteLine($"{CharCode.First()}{CharCode.Last()}");

            //Codes.Add(int.Parse($"{CharCode.First()}{CharCode.Last()}"));
        }

        Console.WriteLine("Part 2: " + Codes.Sum());

    }

    public static void Day1v2()
    {
        var input = Functions.GetInput(1);

        Console.WriteLine("Answer 1: " + SolveD1(input, @"\d"));
        Console.WriteLine("Answer 2: " + SolveD1(input, @"\d|one|two|three|four|five|six|seven|eight|nine"));
    }

    private static int SolveD1(string[] input, string regex)
    {
        int result = 0;
        foreach (string item in input)
        {
            int first = ParseValuesD1(Regex.Match(item, regex).Value);
            int last = ParseValuesD1(Regex.Match(item, regex, RegexOptions.RightToLeft).Value);


            //Console.WriteLine(first + " " + last);
            result += first * 10 + last;
        }

        return result;
    }

    private static int ParseValuesD1(string str) => str switch
    {
        "" => 0,
        "one" => 1,
        "two" => 2,
        "three" => 3,
        "four" => 4,
        "five" => 5,
        "six" => 6,
        "seven" => 7,
        "eight" => 8,
        "nine" => 9,
        var d => int.Parse(d),
    };

    public static void Day2()
    {
        var input = Functions.GetInput(2);

        // 12 red cubes, 13 green cubes, and 14 blue cubes

        int red = 12, green = 13, blue = 14;

        List<int> PossibleGames = [];

        int CurrentGame = 1;


        // Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

        foreach (string item in input)
        {
            bool possible = true;
            var Rounds = item.Replace($"Game {CurrentGame}: ", "").Split(";");

            //Console.WriteLine(item);

            // 3 blue, 4 red
            foreach (var round in Rounds)
            {
                //Console.WriteLine(round);

                var set = round.Split(", ");

                // 3 blue
                foreach (var values in set)
                {
                    var things = values.Trim().Split(" ");

                    int NumOfCubes = int.Parse(things[0].ToString());

                    switch (things[1].ToString())
                    {
                        case "red":
                            if (NumOfCubes > red)
                                possible = false;
                            break;

                        case "green":
                            if (NumOfCubes > green)
                                possible = false;
                            break;

                        case "blue":
                            if (NumOfCubes > blue)
                                possible = false;
                            break;
                    }
                }
            }

            if (possible)
                PossibleGames.Add(CurrentGame);

            CurrentGame++;
        }

        Console.WriteLine("Answer 1:");
        Console.WriteLine(PossibleGames.Sum());


        CurrentGame = 1;

        List<int> GamePowers = [];

        // Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

        foreach (string item in input)
        {
            var Rounds = item.Replace($"Game {CurrentGame}: ", "").Split(";");

            //Console.WriteLine(item);

            int MaxRed = 0, MaxGreen = 0, MaxBlue = 0;


            // 3 blue, 4 red
            foreach (var round in Rounds)
            {
                //Console.WriteLine(round);

                var set = round.Split(", ");

                // 3 blue
                foreach (var values in set)
                {
                    var things = values.Trim().Split(" ");

                    int NumOfCubes = int.Parse(things[0].ToString());

                    switch (things[1].ToString())
                    {
                        case "red":
                            if (NumOfCubes > MaxRed)
                                MaxRed = NumOfCubes;
                            break;

                        case "green":
                            if (NumOfCubes > MaxGreen)
                                MaxGreen = NumOfCubes;
                            break;

                        case "blue":
                            if (NumOfCubes > MaxBlue)
                                MaxBlue = NumOfCubes;
                            break;
                    }
                }
            }

            GamePowers.Add(MaxRed * MaxGreen * MaxBlue);
            CurrentGame++;
        }

        Console.WriteLine("Answer 2:");
        Console.WriteLine(GamePowers.Sum());
    }

    struct CardScore
    {
        public int ID;
        public int Matches;
        public int CardsInInventory;
    }


    // 467..114..
    // ...*......
    // ..35..633.
    // ......#...
    // 617*......
    // .....+.58.
    // ..592.....
    // ......755.
    // ...$.*....
    // .664.598..

    struct EnginePart
    {
        public int ID { get; set; }
        public int Row { get; set; }
        public int Collumn { get; set; }

        public EnginePart(int Id, int row, int position)
        {
            ID = Id;
            Row = row;
            Collumn = position;
        }
    }

    static bool Adjecent(EnginePart p1, EnginePart p2) =>
        Math.Abs(p2.Row - p1.Row) <= 1 && //vrstica enaka, ena viši al pa ena niži
        p1.Collumn <= p2.Collumn + p2.ID.ToString().Length && //
        p2.Collumn <= p1.Collumn + p1.ID.ToString().Length;

    public static void Day3()
    {
        var input = Functions.GetInput(3);

        List<EnginePart> parts = [];
        List<EnginePart> indicators = [];

        //PART 1

        for (int i = 0; i < input.Length; i++)
        {
            string? line = input[i];
            foreach (Match part in Regex.Matches(line, @"\d+"))
                parts.Add(new EnginePart(int.Parse(part.Value), i, part.Index));

            foreach (Match indicator in Regex.Matches(line, @"[^.0-9]"))
                indicators.Add(new EnginePart(1, i, indicator.Index));
        }

        EnginePart[] allParts = parts.ToArray();
        EnginePart[] allIndicators = indicators.ToArray();

        int solution = 0;
        foreach (EnginePart part in allParts)
        {
            if (allIndicators.Any(I => Adjecent(part, I)))
            {
                solution += part.ID;
            }
            //else
            //Console.WriteLine(part.ID);
        }

        Console.WriteLine($"Answer 1: {solution}");


        // PART 2

        List<EnginePart> Gears = [];

        //PART 1

        for (int i = 0; i < input.Length; i++)
        {
            string? line = input[i];
            foreach (Match Gear in Regex.Matches(line, @"\*"))
                Gears.Add(new EnginePart(1, i, Gear.Index));
        }

        EnginePart[] allGears = Gears.ToArray();

        var solution2 =
            (from gear in allGears
             let MatchingParts = from part in allParts where Adjecent(part, gear) select part
             where MatchingParts.Count() == 2
             select MatchingParts.First().ID * MatchingParts.Last().ID).Sum();
        Console.WriteLine($"Answer 2: {solution2}");
    }

    public static void Day4()
    {
        var input = Functions.GetInput(4);


        List<CardScore> Cards = [];

        int currentCardId = 0;
        // Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        foreach (var Card in input)
        {
            //Console.WriteLine(Card);

            var cleanInput = Regex.Replace(Card, @"Card +\d+:", "").Replace("  ", " "); //remove Game and double spaces 

            var NumberSet = cleanInput.Split(" | ");

            int[] WiningNumbers = NumberSet[0].Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                 .Select(int.Parse).ToArray();

            int matches = WiningNumbers.Intersect(NumberSet[1].Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                 .Select(int.Parse).ToArray()).Count();

            currentCardId++;

            Cards.Add(new CardScore
            {
                ID = currentCardId,
                Matches = matches,
                CardsInInventory = 1
            });
        }

        CardScore[] ProcessedCards = Cards.ToArray();

        // PART 1

        List<int> Scores = [];
        foreach (var Card in ProcessedCards)
        {
            int score = Card.Matches is 0 ? 0 : 1;

            for (int i = Card.Matches; i > 1; i--)
            {
                score *= 2;
            }
            Scores.Add(score);
        }

        //Console.WriteLine(score);
        Console.WriteLine($"1: All scratchacards are worth: \x1b[1m{Scores.Sum()}\u001b[0m points!");

        // PART 2:

        int totalOpenedCards = 0;

        // Ko je ene karte konc ne moreš več it nazaj
        // Zmer ka greš naprej prešteješ kok teh kart 
        // in zračunaš kok se jih doda


        for (int i = 1; i <= ProcessedCards.Length; i++)
        {
            CardScore Card = ProcessedCards.First(c => c.ID == i);

            totalOpenedCards += Card.CardsInInventory; //count how many were opened

            foreach (int y in Enumerable.Range(0, Card.Matches))
            {
                ProcessedCards[Card.ID + y].CardsInInventory += Card.CardsInInventory;
            }
        }

        Console.WriteLine($"You opened total of \x1b[1m{totalOpenedCards * 2}\x1b[0m cards!");

    }

    struct SeedMap
    {
        public long ID { get; set; }
        public long Source { get; set; }
        public long Range { get; set; }

        public SeedMap(long ID, long Source, long Range)
        {
            this.ID = ID;
            this.Source = Source;
            this.Range = Range;
        }

        public override string ToString()
        {
            return $"{ID} {Source} {Range}";
        }

    }

    struct MapGroup
    {
        public long ID { get; set; }
        public SeedMap[] Map { get; set; }

        public MapGroup(long ID, SeedMap[] Map)
        {
            this.ID = ID;
            this.Map = Map;
        }
    }

    struct Seed
    {
        public long ID { get; set; }
        public bool Modified { get; set; }

        public Seed(long ID)
        {
            this.ID = ID;
        }

        public void UpdateNum(long NewNum)
        {
            ID = NewNum;
            Modified = true;
        }

        public void ResetUpdateFlag()
        {
            Modified = false;
        }

    }

    //Doesn't work correctly!
    public static void Day5()
    {
        var input = Regex.Split(Functions.GetInputAllText(5), "\\b\\S*\\s\\S*\\b:");


        List<MapGroup> Groups = [];

        List<Seed> seeds = [];

        foreach (var inpt in input)
        {

            if (inpt.ToLower().Contains("seeds:")) //Parse for seeds
            {
                var sds = inpt.Replace("seeds:", "").Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

                seeds = (from seed in sds select new Seed(long.Parse(seed))).ToList();
                continue;
            }

            var lines = inpt.Split("\n", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries); //12 15 5

            List<SeedMap> maps = []; //Store each separate line (12 15 5)
            foreach (var value in lines)
            {
                var nums = value.Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
                maps.Add(new SeedMap(long.Parse(nums[0]), long.Parse(nums[1]), long.Parse(nums[2])));
            }


            Groups.Add(new MapGroup(Groups.Count, maps.ToArray())); //Store each map (eg. seed - to - soil)
        }

        int cycle = 0;
        foreach (var group in Groups.ToArray()) // Seed to soil
        {
            cycle++;
            Console.WriteLine($"\n=={cycle}==\n");

            foreach (var Map in group.Map) // 12 56 2
            {

                for (int i = 0; i < seeds.Count; i++) //for each seed
                {
                    Console.WriteLine($"{Map.ID} {Map.Source} {Map.Range}\n:::: {seeds[i].ID} <= {Map.Source + Map.Range} | {seeds[i].ID <= Map.Source + Map.Range}\n:::: {Map.Source} <= {seeds[i].ID} | {Map.Source <= seeds[i].ID}");

                    if (!seeds[i].Modified  // Check that seed was not updated yet
                        && seeds[i].ID <= Map.Source + Map.Range //Check that seed is in range
                        && Map.Source <= seeds[i].ID)
                    {
                        var newnum = seeds[i].ID - Map.Source + Map.ID;

                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.WriteLine($"{seeds[i].ID} -> {newnum}");
                        Console.ResetColor();

                        if (newnum != seeds[i].ID)
                            seeds[i].UpdateNum(newnum); // Change seed number to soil number, soil number to ...
                    }
                    else
                        Console.WriteLine($"{seeds[i].ID} -> {seeds[i].ID} ");

                }

                if (seeds.All(s => s.Modified))
                    continue;
            }

            seeds.ForEach(s => s.ResetUpdateFlag());
        }

        Console.WriteLine($"Plant seed on location {seeds.Min(s => s.ID)}");

    }

    public static void Day6()
    {
        var input = Functions.GetInput(6);

        ulong[] times = input[0].Split(":")[1]
            .Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(ulong.Parse).ToArray();

        ulong[] distances = input[1].Split(":")[1]
            .Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
            .Select(ulong.Parse).ToArray();


        ulong solution = 0;

        for (int i = 0; i < distances.Length; i++)
        {
            var diff = HoldTIme(times[i], distances[i]);

            _ = solution is 0 ? solution = diff : solution *= diff;
        }

        Console.WriteLine($"Part 1: {solution}");

        // Part 2:

        ulong time = ulong.Parse(input[0].Split(":")[1].Replace(" ", "").Trim());
        ulong distance = ulong.Parse(input[1].Split(":")[1].Replace(" ", "").Trim());

        //ulong time = 71530;
        //ulong distance = 940200;

        Console.WriteLine(time);
        Console.WriteLine(distance);

        Console.WriteLine("Part 2: " + HoldTIme(time, distance));

    }

    private static ulong HoldTIme(ulong TotalTime, ulong DistanceToBeat)
    {
        //Console.WriteLine($"t = {TotalTime} x = {DistanceToBeat}");

        ulong count = 0;
        for (ulong t_c = 0; t_c <= TotalTime; t_c++)
        {
            var distance = -Math.Pow(t_c, 2) + TotalTime * t_c;

            //Console.WriteLine($"x({t_c}) = {distance}");

            if (distance > DistanceToBeat)
                count++;
        }
        return count;
    }

    struct Node
    {
        public string ID { get; set; }
        public string Left { get; set; }
        public string Right { get; set; }

        public Node(string ID, string Left, string Right)
        {
            this.ID = ID;
            this.Left = Left;
            this.Right = Right;
        }

        public override string ToString()
        {
            return $"{ID} -> [{Left} {Right}]";
        }
    }

    public static void Day8()
    {
        var input = Functions.GetInput(8);

        char[] directions = [];
        List<Node> nodes = [];

        for (int i = 0; i < input.Length; i++)
        {
            if (i == 0)
            {
                directions = input[i].ToCharArray();
                continue;
            }
            if (input[i].Length == 0)
                continue;

            string[]? line = Regex.Replace(input[i], @"[()]", "").Split("=", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
            //AAA = (BBB, CCC)


            string ID = line[0];
            line = line[1].Split(",");

            string left = line[0].Trim();
            string right = line[1].Trim();

            nodes.Add(new Node(ID, left, right));

            //Console.WriteLine(nodes.Last());
        }


        // PART 1

        Node CurrentNode = nodes.Find(n => n.ID == "AAA");
        long solution = 0;

        bool escaped = false;
        while (!escaped)
        {

            foreach (char dir in directions)
            {
                //Console.WriteLine($"turn {(dir is 'L'? "left" : "right")}");


                if (dir == 'L')
                    CurrentNode = nodes.First(n => n.ID == CurrentNode.Left);
                else if (dir == 'R')
                    CurrentNode = nodes.First(n => n.ID == CurrentNode.Right);

                //Console.WriteLine($"{CurrentNode.ID}");

                solution++;

                if (CurrentNode.ID == "ZZZ")
                {
                    escaped = true;
                    break;
                }

            }

            //escaped = true;
            //Console.WriteLine("Loop");
        }

        Console.WriteLine($"It took {solution} steps to escape!");


        // PART 2

        List<Node> CurrentNodes = nodes.Where(n => n.ID.EndsWith("A")).ToList();
        List<long> EscapeSteps = [];

        escaped = false;
        solution = 0;

        while (CurrentNodes.Count > 0)
            foreach (char dir in directions)
            {
                //Console.WriteLine($"turn {(dir is 'L'? "left" : "right")}");

                for (int i = 0; i < CurrentNodes.Count; i++)
                {
                    if (dir == 'L')
                        CurrentNodes[i] = nodes.First(n => n.ID == CurrentNodes[i].Left);
                    else if (dir == 'R')
                        CurrentNodes[i] = nodes.First(n => n.ID == CurrentNodes[i].Right);

                    //Console.WriteLine($"{CurrentNode.ID}");
                }

                solution++;



                for (int i = 0; i < CurrentNodes.Count; i++)
                {
                    if (CurrentNodes[i].ID.EndsWith("Z"))
                    {
                        EscapeSteps.Add(solution);
                        CurrentNodes.RemoveAt(i);
                    }
                }

                if (CurrentNodes.Count == 0)
                    break;
            }


        Console.WriteLine(string.Join(Environment.NewLine, EscapeSteps));

        int test = 10 + (int)Math.Pow(10, 300);

        //escaped = true;
        //Console.WriteLine("Loop");

        solution = Lcm(EscapeSteps);

        Console.WriteLine($"It took {solution} steps to escape!");



    }

    static long Gcd(long num1, long num2)
    {
        if (num2 == 0)
            return num1;
        return Gcd(num2, num1 % num2);
    }

    static long Lcm(List<long> arr)
    {
        long lcm = arr[0];
        for (int i = 1; i < arr.Count; i++)
        {
            long num1 = lcm;
            long num2 = arr[i];
            long gcdVal = Gcd(num1, num2);
            lcm = (lcm * arr[i]) / gcdVal;
        }
        return lcm;
    }

    public static void Day9()
    {
        var input = Functions.GetInput(9);

        List<int> Solution1 = [];
        List<int> Solution2 = [];

        foreach (var item in input)
        {

            List<int[]> LowerSets = [];
            LowerSets.Add(item.Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select(int.Parse).ToArray());

            while (true)
            {
                var set = GenerateLowerSequence([.. LowerSets.Last()]);

                if (set.All(x => x == 0))
                    break;

                LowerSets.Add(set);
            }

            int NextValue = 0;
            int PreveriousValue = 0;

            for (int i = LowerSets.Count - 1; i >= 0; i--)
            {
                NextValue += LowerSets[i].Last();
                //Console.WriteLine(NextValue);
            }

            for (int i = LowerSets.Count - 1; i >= 0; i--)
            {
                if (i == LowerSets.Count - 1)
                    PreveriousValue = LowerSets[i].First();
                else
                    PreveriousValue = LowerSets[i].First() - PreveriousValue;

            }

            Solution1.Add(NextValue);
            Solution2.Add(PreveriousValue);
            //Console.WriteLine(PreveriousValue);


            //Console.WriteLine(NextValue);
        }

        Console.WriteLine($"Solution1: {Solution1.Sum()}");
        Console.WriteLine($"Solution2: {Solution2.Sum()}");
    }

    private static int[] GenerateLowerSequence(int[] In)
    {

        List<int> values = [];

        for (int i = 0; i < In.Length - 1; i++)
        {
            values.Add(In[i + 1] - In[i]);
        }

        return [.. values];
    }

    public static void Day13()
    {
        var input = Functions.GetInputAllText(13);

        string[] maps = input.Split("\r\n\r\n", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
 
        // First go over all lines up to down and check for mirror line, then rotate map and repeat

        Complex c = Complex.ImaginaryOne;

        Console.WriteLine(c + 2);
        

    }

    public static void Day14()
    {
        var input = Functions.GetInput(14);

        // Load rocks

        int[,] Platform = input.ParsePlatform();


        int[,] OriginalState = Platform;

        Console.WriteLine($"Total load on north support after tilting to north: {GetTotalLoad(TiltPlatform(Platform))}");

        Platform = OriginalState;

        // PART 2

        // Rocks will eventually begin to loop
        List<string> History = [];

        for (int cycle = 1_000_000_000; cycle >= 0; cycle--)
        {
            Platform = PlatformCycle(Platform);
            Console.WriteLine(GetTotalLoad(Platform));

            string platformString = Platform.PrintPlatform(false);

            int LoopStart = History.IndexOf(platformString);

            if (LoopStart != -1)
            {
                int loopLength = History.Count - LoopStart;
                int Remainder = cycle % loopLength;
                Platform = History[Remainder + LoopStart-1]
                    .Split("\n", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                    .ParsePlatform();
                break;
                //var loopLength = history.Count - idx;
                //var remainder = count % loopLength;
                //return Parse(history[idx + remainder]);
            }
            else
                History.Add(platformString);

        }

        Console.WriteLine($"---");

        Console.WriteLine($"Total load on north support after 1 000 000 000 cycles: {GetTotalLoad(Platform)}");
        
    }
    
    private static int[,] ParsePlatform(this string[] input)
    {
        int[,] Platform = new int[input.Length, input[0].Length];

        for (int i = 0; i < input.Length; i++)
        {
            for (int j = 0; j < input[i].Length; j++)
            {
                Platform[i, j] = input[i][j] switch
                {
                    'O' => 0, // ROUND ROCK
                    '.' => 1, // EMPTY TILE
                    '#' => 2, // CUBE
                    _ => throw new Exception("Ya got wrong input file!")
                };
            }
        }

        return Platform;
    }

    private static int[,] PlatformCycle(this int[,] Platform)
    {
        for (int i = 0; i < 4; i++)
        {
            Platform = TiltPlatform(Platform).Rotate();
        }

        return Platform;
    }

    private static int[,] TiltPlatform(this int[,] Platform)
    {
        // TILT
        for (int collumn = 0; collumn < Platform.GetLength(1); collumn++) // Move from left to right
        {
            int FreeRow = 0;

            for (int row = 0; row < Platform.GetLength(0); row++) // Move from north to south
            {
                if (Platform[row, collumn] == 2)
                    FreeRow = row + 1; // If there is a cube, next rock can roll one row higher
                else if (Platform[row, collumn] == 0)
                {
                    Platform[row, collumn] = 1;
                    Platform[FreeRow, collumn] = 0; // Roll a rock to first free row
                                                    //PrintPlatform(Platform, FreeRow, collumn);
                    FreeRow++;
                }
            }
        }

        return Platform;
    }

    private static int GetTotalLoad(this int[,] Platform)
    {
        int TotalLoad = 0;
        for (int i = 0; i < Platform.GetLength(0); i++)
        {
            for (int j = 0; j < Platform.GetLength(1); j++)
            {
                if (Platform[i, j] != 0)
                    continue;

                // Load of one rock is number of rows counted from south;

                TotalLoad += Platform.GetLength(0) - i;

            }
        }

        return TotalLoad;
    }

    private static string PrintPlatform(this int[,] Platform, bool print = true)
    {

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < Platform.GetLength(0); i++)
        {
            for (int j = 0; j < Platform.GetLength(1); j++)
            {
                sb.Append(Platform[i, j] switch
                {
                    0 => "O", // ROUND ROCK
                    1 => ".", // EMPTY TILE
                    2 => "#", // CUBE
                    _ => throw new Exception("Wut")
                });
            }
            sb.AppendLine();
        }
        if (print)
        {
            Console.WriteLine("Current situation:");
            Console.WriteLine(sb);
        }
        
        return sb.ToString();
    }

    public static void Day15()
    {
        string[] input = Functions.GetInputAllText(15)
            .Replace("\n", "")
            .Split(",", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

        List<int> InitializationValues = [];

        foreach (string instruction in input)
            InitializationValues.Add(HASH(instruction));

        Console.WriteLine($"HASH algorythm returns: {InitializationValues.Sum()}");


        // PART 2

        List<Lens>[] Boxes = new List<Lens>[256];

        for (int i = 0; i < Boxes.Length; i++)
        {
            Boxes[i] = new List<Lens>();
        }

        // MOVE LENSES AROUND

        foreach (var instr in input)
        {
            Lens lens = new(instr);

            if (instr.Contains("-"))
                Boxes[lens.HASH].Remove(Boxes[lens.HASH].Find(l => l.Label == lens.Label));
            else
            {
                if (Boxes[lens.HASH].Any(b => b.Label == lens.Label))
                {
                    int index = Boxes[lens.HASH].FindIndex(b => b.Label == lens.Label);
                    Boxes[lens.HASH][index] = lens; //replace old lens with new one without moving anythin in box
                }
                else
                    Boxes[lens.HASH].Add(lens);
            }


        }

        // Calculate focusing power
        int focusingPower = 0;

        foreach (var box in Boxes)
        {
            for (int i = 0; i < box.Count; i++)
            {
                Lens lens = box[i];
                int par1 = 1 + lens.HASH;
                int par2 = 1 + i;

                focusingPower += par1 * par2 * lens.FocalLength;
            }
        }

        Console.WriteLine($"Focusing power of current arrangement: {focusingPower}");
    }

    private struct Lens
    {
        public string Label { get; set; }
        public int HASH { get; set; }
        public int FocalLength { get; set; }

        public Lens(string instr)
        {
            string[] inst = Regex.Split(instr, "[=-]").Where(d => d.Length != 0).ToArray();

            Label = inst.First();
            HASH = HASH(Label);
            FocalLength = inst.Count() is 2 ? int.Parse(inst.Last()) : 0;
        }
    }



    private static int HASH(string input)
    {
        int currentValue = 0;

        foreach (char c in input)
        {
            currentValue += (int)c;
            currentValue *= 17;
            currentValue %= 256; // Get the remainder
        }

        return currentValue;
    }
}

