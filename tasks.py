from invoke import task

@task
def start(ctx):
  ctx.run('python3 src/app.py', pty=True)

@task
def test(ctx):
  ctx.run('pytest src/', pty=True)

@task
def coverage(ctx):
  ctx.run('coverage run --branch -m pytest src/', pty=True)

@task(coverage)
def coverage_report(ctx):
  ctx.run('coverage html', pty=True)

@task
def db(ctx):
  ctx.run('cat schema.sql | sqlite3 elokuvat.db')
