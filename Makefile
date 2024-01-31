all: clean compile

change-version:
	bin/change-version.sh $(version)

compile:
	bin/compile.sh $(version)

package:
	bin/package.sh

deploy:
	bin/deploy.sh

test:
	bin/test.sh

playground-up:
	bin/playground-up.sh

playground-down:
	bin/playground-down.sh

clean:
	bin/clean.sh
