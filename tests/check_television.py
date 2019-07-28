from pytest import mark


# tests will run for each param / tuple in the list - here 3 brands
@mark.parametrize('tv_brand', [
    ('Samsung'),
    ('Sony'),
    ('Visio'),
])
def check_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")