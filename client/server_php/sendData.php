<?php
    $doc = new DOMDocument();
    $root = $doc->createElement('root');
    $doc->appendChild($root);
    $from = $doc->createElement('from');
    $from->nodeValue = 'http://www.example.com/';
    $from->setAttribute('name', 'Newyork');
    $root->appendChild($from);
    $doc->save('node.xml');
    echo $doc->saveXML();




?>