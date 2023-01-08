<?php
    
    
    
    

    

    
    $doc = new DOMDocument();
    $annotation = $doc->createElement('annotation');
    $annotation = $doc->appendChild($annotation);

    
    $folder = $doc->createElement('folder','di_thang');
    $filename = $doc->createElement('filename', 'di_thang_0.png');

    $path = $doc->createElement('path', 'D:\Code\Tensorflow\Collecting Image\datasets_xetuhanh\di_thang\di_thang_0.png');

    $source = $doc->createElement('source');
    $database = $doc->createElement('database', 'dfadfa');
    $database = $source->appendChild($database);


    $size = $doc->createElement('size');
    $width = $doc->createElement('width', 'dfadfaf');
    $width = $size->appendChild($width);
    
    $height = $doc->createElement('height', 'dfadfaf');
    $height = $size->appendChild($height);
    $depth = $doc->createElement('depth', 'dfadfaf');
    $depth = $size->appendChild($depth);




    $segmented = $doc->createElement('segmented', '0');

    $object= $doc->createElement('object');
    $name = $doc->createElement('name', 'di thang');
    $name = $object->appendChild($name);

    $pose = $doc->createElement('pose', 'di thang');
    $pose = $object->appendChild($pose);

    $truncated = $doc->createElement('truncated', 'di thang');
    $truncated = $object->appendChild($truncated);

    $difficult = $doc->createElement('difficult', 'di thang');
    $difficult = $object->appendChild($difficult);


    $bndbox = $doc->createElement('bndbox');
    $bndbox = $object->appendChild($bndbox);

    $xmin = $doc->createElement('xmin', 'dfajdfkkd');
    $xmin = $bndbox->appendChild($xmin);
    $ymin = $doc->createElement('ymin', 'dfajdfkkd');
    $ymin = $bndbox->appendChild($ymin);
    $xmax = $doc->createElement('xmax', 'dfajdfkkd');
    $xmax  = $bndbox->appendChild($xmax);
    $ymax = $doc->createElement('ymax', 'dfajdfkkd');
    $ymax = $bndbox->appendChild($ymax);




    $folder = $annotation->appendChild( $folder);
    $filename = $annotation->appendChild($filename );

    $path = $annotation->appendChild($path);

    $source = $annotation->appendChild( $source);

    $size = $annotation->appendChild( $size);

    $segmented = $annotation->appendChild($segmented);

    $object= $annotation->appendChild($object);





    $doc->save('testkdjkfj.xml');

?>