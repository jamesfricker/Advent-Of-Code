#include <fstream>
#include <iostream>
#include <string>

int solve_a(std::string_view input)
{
    int sum = 0;
    for (u_long i = 0; i < input.length(); i++)
    {
        int next = (i + 1) % input.length();
        if (input[i] == input[next])
        {
            // std::cout << input[i] << '\n';
            sum += input[i] - '0';
        };
    }
    return sum;
}

int solve_b(std::string_view input)
{
    int sum = 0;
    int half = input.length() / 2;
    for (u_long i = 0; i < input.length(); i++)
    {
        int next = (i + half) % input.length();
        if (input[i] == input[next])
        {
            // std::cout << input[i] << '\n';
            sum += input[i] - '0';
        };
    }
    return sum;
}

struct TestCase
{
    std::string_view input;
    int expected;
};

int failed_test(TestCase test, int actual)
{
    std::cerr
        << "FAIL: input " << test.input
        << ", expected " << test.expected
        << ", got " << actual << '\n';
}

bool run_tests()
{
    constexpr TestCase tests_a[] = {
        {"1122", 3},
        {"1111", 4},
        {"1234", 0},
        {"91212129", 9},
    };

    constexpr TestCase tests_b[] = {
        {"1212", 6},
        {"1221", 0},
        {"123425", 4},
        {"123123", 12},
        {"12131415", 4}};

    bool all_passed = true;

    for (const TestCase &test : tests_a)
    {
        int actual = solve_a(test.input);
        if (actual != test.expected)
        {
            failed_test(test, actual);

            all_passed = false;
        }
    }
    for (const TestCase &test : tests_b)
    {
        int actual = solve_b(test.input);
        if (actual != test.expected)
        {
            failed_test(test, actual);

            all_passed = false;
        }
    }
    return all_passed;
}

int main()
{
    if (!run_tests())
    {
        return 1;
    }
    std::ifstream input_file("input.txt");

    if (!input_file)
    {
        std::cerr << "Error: Cannot open input\n";
        return 1;
    }

    std::string input;
    std::getline(input_file, input);

    std::cout << solve_a(input) << '\n';
    std::cout << solve_b(input) << '\n';

    return 0;
}
