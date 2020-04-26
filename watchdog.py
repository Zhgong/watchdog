import click
import os
from datetime import datetime
import time


def get_last_modified_timestamp(file) -> float:
    """Get information of file: it was changed x seconds agao"""
    modified_timestamp = os.path.getmtime(
        file)  # float,which represents the number of seconds since the epoch, epoch is January 1, 1970, 00:00:00 (UTC).
    modified_time = time.ctime(modified_timestamp)
    click.echo(f"modified time: {modified_time}")

    now = datetime.now()
    # convert current time to timestamp, seconds(float) since epoch.
    now_timestamp = now.timestamp()
    click.echo(f"current time: {time.ctime(now_timestamp)}")
    click.echo(f"{now_timestamp}")

    return now_timestamp - modified_timestamp


@click.command()
@click.argument('file', nargs=1, type=click.Path(exists=True))
@click.argument('seconds', type=click.INT)
@click.option('--cmd', "-c", type=click.STRING, help="command to be executed")
def watch(file, seconds, cmd):
    """Simple program that monitor FILE, which should be change in last SECONDS.

    FILE: Path to file

    SECONDS: Seconds(INT)
    
    """
    click.echo('%s; %s!' % (file, seconds))
    delta_to_last_modified = get_last_modified_timestamp(file)
    if delta_to_last_modified > seconds:
        click.echo(
            f"[EXCEED] File has been refreshed in last {seconds} ago! '{cmd}' will be executed")
        os.system(cmd)

    else:
        click.echo(f"[OK] File has been refreshed last {seconds} seconds !")


if __name__ == '__main__':
    watch()
