import click

from gitctx import GitCTX

gitctx = GitCTX()


@click.group()
def cli():
    """
    Click entry command
    :return:
    """


@cli.command(short_help="Create a new gitcontext")
@click.argument("context_name", type=click.STRING)
@click.option("--user-name", type=click.STRING)
@click.option("--user-email", type=click.STRING)
def create(context_name: str, user_name: str, user_email: str):
    gitctx.create(context_name=context_name, user_name=user_name, user_email=user_email)


@cli.command(short_help="Change the active context")
@click.argument("context_name", type=click.STRING)
def use(context_name: str):
    gitctx.use(context_name=context_name)


@cli.command(short_help="Update a context with new configuration")
@click.argument("context_name", type=click.STRING)
@click.option("--user-name", type=click.STRING)
@click.option("--user-email", type=click.STRING)
def update(context_name: str, user_name: str, user_email: str):
    gitctx.update(context_name=context_name, user_name=user_name, user_email=user_email)


@cli.command(short_help="Delete a gitcontext by its context_name")
@click.argument("context_name", type=click.STRING)
def delete(context_name: str):
    gitctx.delete(context_name=context_name)


@cli.command(short_help="Show the current gitcontext")
# @click.option("--fields", type=click.STRING, multiple=True, required=False)
def show(fields: list[str] = None):
    gitctx.show(fields=fields)


@cli.command(name="list", short_help="List all available gitcontexts")
def list_(fields: list[str] = None):
    gitctx.list()


cli()
