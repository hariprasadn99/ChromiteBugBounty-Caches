# ChromiteBugBounty-Caches

This repository contains the tests that are required to be performed for testing the Cache Subsystems of the Chromite Core by InCore Semiconductors.

## The tests that will be done are as follows - 

1. To check if fence and fence.i work properly.
2. To perform cache line thrashing
3. To perform Load hit
4. To perform Store hit

For the first test, a simple addition of two numbers is performed. First, the fence instruction is called where the cache is cleared. Then two registers are loaded with a certain value after which addition is performed with the sum being stored in another register. Lastly, the fence.i instruction is called where the instructions that are present in the cache are cleared.

For the second test, an immediate is loaded into a single register and repeated operations are being performed using the same register which results in excessive usage of the register. This result in line thrashing of the cache.

For the third test, words are loaded to a single address multiple times, basically updating the Load Buffer. This ensures that two words are not assumed to be referred to different memory locations resulting in a load hit.

For the fourth test, a similar approach is considered as compared to the third test but with words being stored instead of being loaded, thereby resulting in a store hit.

## Contributors

1. Hariprasad N (hariprasadn99@gmail.com)
2. Natasha Bonala (natashajessica567@gmail.com)
