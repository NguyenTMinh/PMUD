<?php
    //lưu file ảnh
    $data = json_decode(file_get_contents('php://input'), true);
    $imageData = base64_decode(preg_replace('#^data:image/\w+;base64,#i', '', $data[5]));
    $randomNumber = mt_rand(1, 1000000000);
    $string = strval($randomNumber);

    $x = utf8_encode(strval($data[0]));
    $y = utf8_encode(strval($data[1]));
    $z = utf8_encode(strval($data[2] + $data[0]));

    $t = utf8_encode(strval($data[3] + $data[1]));
    $input = utf8_encode(strval($data[4]));
    
    $nameImg = utf8_encode($input.'_' .$randomNumber);

    if (!file_exists('../dataTrain/'.$input)) {
        mkdir('../dataTrain/'.$input, 0777);
    }
    file_put_contents('../dataTrain/'.$input.'/'.$nameImg.'.png', $imageData);



    //lưu file xml
    $doc = new DOMDocument();
    $annotation = $doc->createElement('annotation');

    
    $folder = $doc->createElement('folder', $input);
    $filename = $doc->createElement('filename', $nameImg);

    $path = $doc->createElement('path', '');

    $source = $doc->createElement('source');
    $database = $doc->createElement('database', 'Unknown');
    $database = $source->appendChild($database);


    $size = $doc->createElement('size');
    $width = $doc->createElement('width', '640');
    $width = $size->appendChild($width);
    
    $height = $doc->createElement('height', '480');
    $height = $size->appendChild($height);
    $depth = $doc->createElement('depth', '3');
    $depth = $size->appendChild($depth);




    $segmented = $doc->createElement('segmented', '0');

    $object= $doc->createElement('object');
    $name = $doc->createElement('name', $input);
    $name = $object->appendChild($name);

    $pose = $doc->createElement('pose', 'Unspecified');
    $pose = $object->appendChild($pose);

    $truncated = $doc->createElement('truncated', '0');
    $truncated = $object->appendChild($truncated);

    $difficult = $doc->createElement('difficult', '0');
    $difficult = $object->appendChild($difficult);


    $bndbox = $doc->createElement('bndbox');
    $bndbox = $object->appendChild($bndbox);

    $xmin = $doc->createElement('xmin', $x);
    $xmin = $bndbox->appendChild($xmin);
    $ymin = $doc->createElement('ymin', $y);
    $ymin = $bndbox->appendChild($ymin);
    $xmax = $doc->createElement('xmax', $z);
    $xmax  = $bndbox->appendChild($xmax);
    $ymax = $doc->createElement('ymax', $t);
    $ymax = $bndbox->appendChild($ymax);




    $folder = $annotation->appendChild( $folder);
    $filename = $annotation->appendChild($filename );

    $path = $annotation->appendChild($path);

    $source = $annotation->appendChild( $source);

    $size = $annotation->appendChild( $size);

    $segmented = $annotation->appendChild($segmented);

    $object= $annotation->appendChild($object);



    $annotation = $doc->appendChild($annotation);


 

    $doc->save(utf8_encode('../dataTrain/'.$input.'/'.$nameImg.'.xml'));
    


?>