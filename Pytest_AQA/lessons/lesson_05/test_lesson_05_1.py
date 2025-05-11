class TestClassA1:
    def test_func_a11(self, function_scope, class_scope, module_scope, package_scope, session_scope):
        assert True

    def test_func_a12(self, function_scope, class_scope, module_scope, package_scope, session_scope):
        assert True


class TestClassB1:
    def test_func_b11(self, function_scope, class_scope, module_scope, package_scope, session_scope):
        assert True

    def test_func_b12(self, function_scope, class_scope, module_scope, package_scope, session_scope):
        assert True
