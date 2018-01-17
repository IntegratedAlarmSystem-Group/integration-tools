package org.dasu;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Properties;

import org.eso.ias.cdb.json.CdbJsonFiles;
import org.eso.ias.cdb.CdbReader;
import org.eso.ias.cdb.json.JsonReader;
import org.eso.ias.dasu.subscriber.KafkaSubscriber;
import org.eso.ias.dasu.Dasu;
import org.eso.ias.dasu.publisher.KafkaPublisher;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

class DasuTest {

    public static void main(String[] args) throws IOException {

        System.setProperty("log_file_name", DasuTest.class.getSimpleName());
        Logger logger = LoggerFactory.getLogger(DasuTest.class);

        // Build the CDB reader
        Path cdbParentPath = FileSystems.getDefault().getPath(".");
        CdbJsonFiles cdbFiles = new CdbJsonFiles(cdbParentPath);
        CdbReader cdbReader = new JsonReader(cdbFiles);

        // define the variables to process in the dasus
        String[] vars = {"Temperature", "Pressure", "WindDirection",
                "WindSpeed", "Humidity", "Dewpoint"};
        int[] ids = {2};

        String[] dasuIds = new String[vars.length * ids.length];
        for (int i = 0; i < ids.length; i++) {
            for (int j = 0; j < vars.length; j++) {
                dasuIds[i * vars.length + j] = "Dasu" + vars[j] + ids[i];
            }
        }

        System.out.println(Arrays.toString(dasuIds));

        ArrayList<Dasu> dasus = new ArrayList<>();

        logger.info("Creating the dasus");
        for (String id : dasuIds) {
            KafkaPublisher outputPublisher = KafkaPublisher.apply(id, new Properties());
            KafkaSubscriber inputsProvider = new KafkaSubscriber(id, new Properties());

            // The DASU
            Dasu dasu = new Dasu(id, outputPublisher, inputsProvider, cdbReader);
            dasus.add(dasu);
        }

        // Start the getting of events in the DASUs
        logger.info("Starting the dasus.");
        for (Dasu dasu : dasus) {
            dasu.start();
        }

        while (true) {
            // run DASUs permanently
        }
    }
}
