class TestClassA2:
    def test_func_a21(self, function_scope, class_scope, module_scope, package_scope, session_scope):
        assert True

    def test_func_a22(self, function_scope, class_scope, module_scope, package_scope, session_scope):
        assert True


class TestClassB2:
    def test_func_b21(self, function_scope, class_scope, module_scope, package_scope, session_scope):
        assert True

    def test_func_b22(self, function_scope, class_scope, module_scope, package_scope, session_scope):
        assert True
