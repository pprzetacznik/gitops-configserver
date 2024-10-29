- my_config:
  - var1: {template_var1}
  - var2: {template_var2}
  - var2: {template_var3}
  - lll: |
    { template_var4 | to_yaml | indent }
  - ccc
