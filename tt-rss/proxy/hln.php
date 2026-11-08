<?php

$section = $_GET['section'] ?? null;
$original_feed_url = "https://www.hln.be/$section/rss.xml";

// 1. Fetch the feed
$xml_string = file_get_contents($original_feed_url);
if (! $xml_string) {
    http_response_code(500);
    exit('Failed to fetch feed.');
}
$dom = new DOMDocument();
// Suppress errors caused by non-standard RSS tags or namespaces
libxml_use_internal_errors(true);
$dom->loadXML($xml_string);
libxml_clear_errors();

$xpath = new DOMXPath($dom);

$items = $dom->getElementsByTagName('item');

foreach ($items as $item) {
    $link_node = $xpath->query('link', $item)->item(0);

    if ($link_node) {
        $link_url = $link_node->nodeValue;
        $guid_node = $xpath->query('guid', $item)->item(0);

        if ($guid_node) {
            $guid_node->nodeValue = "hln-" . preg_replace('/.*~([A-Za-z0-9]*).*/', '$1', $guid_node->nodeValue);
        }
    }
}
header('Content-Type: application/rss+xml; charset=utf-8');
echo $dom->saveXML();
