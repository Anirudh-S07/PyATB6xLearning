class TestCounter:
    count = 0

    def __init__(self):
        TestCounter.count += 1

        self.count += 100


t1 = TestCounter()
t2 = TestCounter()
print(TestCounter.count)
print(t1.count)


# Each time an object is created, count increases.
# count is shared across all objects.
