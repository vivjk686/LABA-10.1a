#include "pch.h"
#include "CppUnitTest.h"
#define UNIT_TEST
#include "../LABA-10.1a/LABA-10.1a.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest101a
{
    TEST_CLASS(UnitTest101a)
    {
    public:
        TEST_METHOD(TestCountPhysicsGrades)
        {
            const int N = 4;
            Student p[N] = {
                { "Kovalenko", 1, KN,  5, 5, 5 },
                { "Ivanenko",  2, INF, 4, 4, 4 },
                { "Petrenko",  1, ME,  3, 5, 4 },
                { "Sydorenko", 3, FI,  5, 3, 5 }
            };
            int c5 = 0, c4 = 0, c3 = 0;
            CountPhysicsGrades(p, N, c5, c4, c3);
            Assert::AreEqual(2, c5);
            Assert::AreEqual(1, c4);
            Assert::AreEqual(1, c3);
        }

        TEST_METHOD(TestCountPhysicsMathHighGrades)
        {
            const int N = 4;
            Student p[N] = {
                { "Kovalenko", 1, KN,  5, 5, 5 },
                { "Ivanenko",  2, INF, 4, 4, 4 },
                { "Petrenko",  1, ME,  3, 5, 4 },
                { "Sydorenko", 3, FI,  5, 3, 5 }
            };
            Assert::AreEqual(2, CountPhysicsMathHighGrades(p, N));
        }
    };
}
