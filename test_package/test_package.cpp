#include <cstdlib>
#include <iostream>
#include <boost/format.hpp>

int main()
{
    std::cout << boost::format("boost format: string value \"%1%\" int value \"%2%\"") % "hello" % 777;
    return EXIT_SUCCESS;
}
