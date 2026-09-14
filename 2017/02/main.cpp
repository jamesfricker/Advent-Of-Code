#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
struct Spreadsheet
{
    std::vector<std::vector<int>> lines;
};

int solve_a(Spreadsheet &input)
{
    int checksum = 0;
    for (int i = 0; i < input.lines.size(); i++)
    {
        int max = input.lines[i][0];
        int min = input.lines[i][0];
        for (int j = 0; j < input.lines[i].size(); j++)
        {
            if (input.lines[i][j] > max)
            {
                max = input.lines[i][j];
            }
            if (input.lines[i][j] < min)
            {
                min = input.lines[i][j];
            }
        }
        checksum += max - min;
    }
    return checksum;
}

int solve_b(Spreadsheet &input)
{
    int result = 0;
    for (int i = 0; i < input.lines.size(); i++)
    {
        std::sort(input.lines[i].begin(), input.lines[i].end());
        for (int j = 0; j < input.lines[i].size(); j++)
        {
            for (int k = 0; k < j; k++)
            {
                int remainder = input.lines[i][j] % input.lines[i][k];
                if (remainder == 0)
                {
                    // found some that are divisible
                    result += input.lines[i][j] / input.lines[i][k];
                }
            }
        }
    }
    return result;
}

Spreadsheet read_input(const char *file_name)
{
    std::ifstream input_file(file_name);

    if (!input_file)
    {
        std::cerr << "Error: Cannot open input\n";
    }

    std::string line;
    Spreadsheet s;
    while (std::getline(input_file, line))
    {
        std::vector<int> row;
        std::istringstream stream(line);
        int number;
        while (stream >> number)
        {
            row.push_back(number);
        }
        s.lines.push_back(row);
    }
    return s;
}

int main()
{

    Spreadsheet s = read_input("input.txt");
    Spreadsheet a = read_input("test_a.txt");
    Spreadsheet b = read_input("test_b.txt");

    // expecting 18
    std::cout << solve_a(a) << "\n";
    std::cout << solve_a(s) << "\n";
    // expecting 9
    std::cout << solve_b(b) << "\n";
    std::cout << solve_b(s) << "\n";

    return 0;
}