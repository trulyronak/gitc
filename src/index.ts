import {Command, flags} from '@oclif/command'
import { exec, ExecException } from "child_process"

class Gitc extends Command {
  static description = 'Instantly push your changes to your Git Remote Repository'
  static strict = false

  static flags = {
    // add --version flag to show CLI version
    version: flags.version({char: 'v'}),
    help: flags.help({char: 'h'}),
    // flag with a value (-n, --name=VALUE)
    name: flags.string({char: 'n', description: 'name to print'}),
    // flag with no value (-f, --force)
    force: flags.boolean({char: 'f'}),
  }

  static args = []

  async run() {
    const {argv} = this.parse(Gitc)
    const message = argv.join(" ");
    this.log(message)
    exec(`git add -A && git commit -m "${message}" && git push`, (error: ExecException | null, stdout: string, stderr: string) => {
      if (error) {
        this.log("Something went wrong:")
        this.log(`${error}`);
      } else {
        this.log(stdout);
      }
    })

  }
}

export = Gitc
