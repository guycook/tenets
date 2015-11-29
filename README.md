# LINGO REVIEWS ALPHA

## House keeping

Thank you for testing lingo in it's infancy. Please open an issue for any bugs or feature requests.

This is Alpha. The libs are woefully under unit tested and have more todos than comments. There will be bugs. At this early stage, we are interested in your assesment of lingo's usefullness and potential.

Okay, with that out of the way, let's get started.

## First Run

### Docker Quick Start

If you have Docker installed, try the following:

```bash
# Put lingo on your path.
mv ./lingo ~/path/to/bin

# Find some source code to review.
cd tenets/go/license/example

# Review the code.
lingo review
# ... wait while tenets are downloaded.

# Read the tenet documentation for this code.
lingo docs

```

When lingo reviews, it looks for a .lingo file in the current or parent directories. If those tenets use a docker driver (default) and no local docker image is found, lingo goes and gets it. All config files are in toml. We will be supporting yaml and json also.


This time, let's start without a .lingo:

```bash
cd tenets/go/simpleseed/example

# This will write a .lingo file.
lingo init

# List avaliable tenets on hub.docker.com:
docker search lingoreviews

# Add the license example:
lingo add lingoreviews/simpleseed

# ... you could add more tenets here.

# Pull down the images from hub.docker.com:
lingo pull

# If you didn't pull, review will do it for you.

# Review the code, this time we'll keep some output at the end:
lingo review --output-format --json-pretty

```

Notes: A better tenet search UI is in the pipeline and tenets can be pulled from any docker repository.

Have a play. You'll see lingo prompts you to open the issue. Supported editors are: vi, vim, emacs, nano and subl.

### Binary Quick Start

Let's build a tenet from source. The following is a fully functional tenet. You'll find it in tenets/go/simpleseed. 


```go

package main

import (
	"go/ast"

	"github.com/lingo-reviews/tenets/go/dev/server"
	"github.com/lingo-reviews/tenets/go/dev/tenet"
)

type commentTenet struct {
	tenet.Base
}

func main() {
	c := &commentTenet{}
	c.SetInfo(tenet.Info{
		Name:     "simpleseed",
		Usage:    "every comment should be awesome",
		Language: "Go",
		Description: "description",
	})

	issue := c.RegisterIssue("sucky_comment", tenet.AddComment("this comment could be more awesome"))
	c.SmellNode(func(r tenet.Review, comment *ast.Comment) error {
		if comment.Text != "// most awesome comment ever" {
			r.RaiseNodeIssue(issue, comment)
		}
		return nil
	})

	server.Serve(c)
}

```

To build:

```bash
cd tenets/go/simpleseed
lingo build
```
You'll see the following output:
```bash
Building Go binary: [/home/you/.lingo_home/tenets/lingoreviews/simpleseed]
binary 1 / 1 [===============================================] 100.00 % 1s
Success! All binary tenets built.

```

You can now add simpleseed to any project. Beacuse it's not docker, we need to specify the driver when we add it:

```bash
lingo add lingoreviews/simpleseed --driver binary
```


`lingo build` looks for a .lingofile for instructions on how to build the tenet. This is the simpleseed .lingofile:

```toml
language = "go"
owner = "lingoreviews"
name = "simpleseed"

[docker]
  build=false
  overwrite_dockerfile=true
```

By default, binary tenets are installed in /home/you/.lingo_home/tenets/[owner]/[name]. This can be overridden with the LINGO_BIN environment variable.

You'll note .lingofile sets docker build to false. If you remove that and run build again, lingo will build both a docker image and a binary. Until github.com/lingo-reviews/tenets/go/dev is published, you'll have to manually check this out before building a docker image.

As you'll likely be writing and updating lots of tenets (we hope!), lingo build provides a --all flag. Try it out:

```bash
cd tenets/go

lingo build --all
```

This looks for all .lingofiles under the current directory and attempts to build all the tenets.

## Options

Some tenets take options. To view their avaliable options run:

```bash
lingo info
```

The imports tenet takes a blacklist_regex option, here's an example of setting it:

```bash
lingo add lingoreviews/imports --options blacklist_regex=".*/State"
```


## Bash completion

To enable bash completion, run the following:

```bash
lingo --generate-bash-completion
```

Commands and some arguments will now autocomplete, in particular installed binary tenet names.


### Writing a Tenet

The `go/tenets` directory has a varity of examples of tenets in Go. Copy one of those to get started. Other languages are possible. All tenets talk to lingo via the API schema defined in api.proto. You can use api.proto to generate the API in one of 10 languages. Visit grpc.io to learn more.

## Hey! Where's my LAAS?

We've recently refactored lingo and need to update Lingo as a Service to work with the new style tenets. Check back here for updates.