from time import sleep
from tests.resources.test_base import TestBase
from investing_algorithm_framework import TimeUnit


def test_func(algorithm):
    TestAlgorithmStart.test_func_has_run = True


class TestAlgorithmStart(TestBase):
    test_func_has_run = False

    def setUp(self):
        super(TestAlgorithmStart, self).setUp()
        self.algo_app.algorithm.schedule(
            test_func, time_unit=TimeUnit.SECONDS, interval=1
        )
        TestAlgorithmStart.test_func_has_run = False
        self.algo_app.algorithm.stop()

    def test_start(self):
        self.assertFalse(TestAlgorithmStart.test_func_has_run)
        response = self.client.get("/start")
        self.assertEqual(200, response.status_code)
        self.assertTrue(self.algo_app.algorithm.running)
        sleep(2)
        self.assertTrue(TestAlgorithmStart.test_func_has_run)

    def test_start_with_already_stopped_algorithm(self):
        self.assertFalse(TestAlgorithmStart.test_func_has_run)
        response = self.client.get("/start")
        self.assertEqual(200, response.status_code)
        self.assertTrue(self.algo_app.algorithm.running)

        response = self.client.get("/start")
        self.assertEqual(400, response.status_code)
        self.assertTrue(self.algo_app.algorithm.running)

        sleep(2)
        self.assertTrue(TestAlgorithmStart.test_func_has_run)

    def tearDown(self):
        self.algo_app.algorithm.stop_all_workers()
        super(TestAlgorithmStart, self).tearDown()
