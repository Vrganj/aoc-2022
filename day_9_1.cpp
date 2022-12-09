#include <iostream>
#include <set>

bool touching(const std::pair<int, int>& a, const std::pair<int, int>& b) {
    int dx = std::abs(a.first - b.first);
    int dy = std::abs(a.second - b.second);

    return dx <= 1 && dy <= 1;
}

int main() {
    std::pair<int, int> head { 0, 0 }, tail { 0, 0 };
    std::set<std::pair<int, int>> visited { tail };

    for (int i = 0; i < 2000; ++i) {
        char direction;
        int amount;

        std::cin >> direction >> amount;

        std::pair<int, int> delta;

        if (direction == 'U') {
            delta = { 0, 1 };
        } else if (direction == 'D') {
            delta = { 0, -1 };
        } else if (direction == 'L') {
            delta = { -1, 0 };
        } else if (direction == 'R') {
            delta = { 1, 0 };
        }

        for (int j = 0; j < amount; ++j) {
            head.first += delta.first;
            head.second += delta.second;

            if (!touching(head, tail)) {
                if (tail.first == head.first) {
                    if (tail.second > head.second) {
                        --tail.second;
                    } else if (tail.second < head.second) {
                        ++tail.second;
                    }
                } else if (tail.second == head.second) {
                    if (tail.first > head.first) {
                        --tail.first;
                    } else if (tail.first < head.first) {
                        ++tail.first;
                    }
                } else {
                    if (tail.first > head.first) {
                        --tail.first;
                    } else if (tail.first < head.first) {
                        ++tail.first;
                    }

                    if (tail.second > head.second) {
                        --tail.second;
                    } else if (tail.second < head.second) {
                        ++tail.second;
                    }
                }

                visited.insert(tail);
            }
        }
    }

    std::cout << visited.size() << std::endl;

    return 0;
}
