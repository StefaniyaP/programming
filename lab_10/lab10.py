import typer

from moduls import character_s_hp, funtion, nd_array

app = typer.Typer()


@app.command()
def n_arr(m: int, n: int):
    print(f'm: {m}, n: {n}\n', nd_array.create_n_dim_array(m, n))


@app.command()
def y_func(k: int, x: int):
    print(f'x: {x}, k: {k}\n', funtion.y(k, x))


@app.command()
def h_p():
    print(character_s_hp.hp())


if __name__ == "__main__":
    app()
