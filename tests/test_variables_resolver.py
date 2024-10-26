from gitops_configserver.templates_rendering import VariablesResolver


def test_variables_resolver():
    template_variables_mapping = [
        {"tenant_variable": "aaa", "tpl_variable": "template.var1"},
        {"tenant_variable": "bbb", "tpl_variable": "template.var2"},
        {"tenant_variable": "ccc", "tpl_variable": "template.var3"},
    ]
    tenant_variables = {
        "aaa": "aaa1.default",
        "bbb": "bbb1.default",
        "ccc": "ccc1.default",
    }
    resolved_variables = VariablesResolver.resolve_for_template(
        template_variables_mapping,
        tenant_variables,
    )
    assert resolved_variables == {
        "template.var1": "aaa1.default",
        "template.var2": "bbb1.default",
        "template.var3": "ccc1.default",
    }
