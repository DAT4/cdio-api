for img in *.jpg
do
    convert "$img" -resize 500x "new/$(basename "$img")" ;
done

