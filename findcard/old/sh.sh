for img in *.jpg
do 
    convert "$img" -resize 500x -rotate 90 "new/$(basename "$img")" ; 
done

