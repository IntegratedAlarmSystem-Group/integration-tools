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

        System.setProperty("log_file_name", ConverterTest.class.getSimpleName());

        // read cdb
        Path cdbParentPath = FileSystems.getDefault().getPath(".");
        CdbJsonFiles cdbFiles = new CdbJsonFiles(cdbParentPath);
        CdbReader cdbReader = new JsonReader(cdbFiles);

        // build the converter
        ConverterKafkaStream stream = new ConverterKafkaStream(converterID, new Properties());
        Converter converter = new Converter(converterID, cdbReader, stream);
        converter.setUp();

        while (true) {
            // run converter
        }
    }
}
