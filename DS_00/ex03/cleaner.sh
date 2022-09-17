#!/bin/sh

FILE=../ex02/hh_sorted.csv

echo '"id","created_at","name","has_test","alternate_url"' > hh_positions.csv

cat $FILE | tail -n +2 "$FILE" | \
    awk \
    'BEGIN{
      FS=OFS="\",";
      Regexes[0] = "[Jj]unior\\+?/?";
      Regexes[2] = "[Jj]unior[+]\\+?/?";
      Regexes[4] = "[Mm]iddle\\+?/?";
      Regexes[6] = "[Ss]enior";
    }
    {
      result = "";
      for (i = 0; i < length(Regexes); ++i)
      {
        match($3, Regexes[i]);
        if (RLENGTH > 0) {
          first_char = substr($3, RSTART, 1);
          result = result toupper(first_char) substr($3, RSTART + 1, RLENGTH - 1);
        }
      }
      if (length(result) == 0) {
        $3 = "\"-";
      }
      else {
        $3 = "\"" result;
      }
      
      print;
    }' \
    >> hh_positions.csv