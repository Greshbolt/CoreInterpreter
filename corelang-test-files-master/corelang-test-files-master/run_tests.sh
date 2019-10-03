#!/bin/sh

if [ "$*" = "" ]
then
  echo Tests not run, missing required arguments
  echo usage: $0 [command_to_run_your_interpreter]
  exit 1
fi

if ! hash ${1%% *} 2>/dev/null
then
  echo Tests not run, could not find command "${1%% *}"
  exit 1
fi

tests="**/*.code"
diff_options="-u"

if diff --color=always empty.data empty.data 2>/dev/null
then
  diff_options="-u --color=always"
fi

for t in $tests
do
  t=${t%\.code}
  code=$t.code
  data=$t.data
  expected=$t.expected

  if [ ! -f $data ]
  then
    data=empty.data
  fi

  printf "Testing %s... " "$t"

  if [ $t != "${t%bad*}" ]
  then
    output=$($* $code $data)
    if [ "$output" != "${output%ERROR:*}" ]
    then
      printf "\033[0;32mPASSED\033[0m\n"
    else
      printf "\033[0;31mFAILED\033[0m\n"
      printf "\033[1mexpected error, got following output:\033[0m\n"
      echo "$output"
    fi
  else
    output=$($* $code $data | diff $diff_options - $expected)
    if [ $? -eq 0 ]
    then
      printf "\033[0;32mPASSED\033[0m\n"
    else
      printf "\033[0;31mFAILED\033[0m\n"
      echo "$output"
    fi
  fi
done
