package org.dasu;

import org.eso.ias.cdb.CdbReader;
import org.eso.ias.cdb.IasCdbException;
import org.eso.ias.cdb.json.CdbJsonFiles;
import org.eso.ias.cdb.json.JsonReader;
import org.eso.ias.converter.Converter;
import org.eso.ias.converter.ConverterKafkaStream;
import org.eso.ias.converter.config.ConfigurationException;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.util.Properties;

public class ConverterTest {

    public static void main(String[] args) throws IasCdbException, IOException, ConfigurationException {

        String converterID = "KafkaConverterId";

        Path cdbParentPath = FileSystems.getDefault().getPath("dasu-demo");
        CdbJsonFiles cdbFiles = new CdbJsonFiles(cdbParentPath);
        CdbReader cdbReader = new JsonReader(cdbFiles);

        // Finally builds the converter
        Converter converter = new Converter(converterID, cdbReader, new ConverterKafkaStream(converterID, new Properties()));

        converter.setUp();

        while (true) {
            // run
        }
    }
}
