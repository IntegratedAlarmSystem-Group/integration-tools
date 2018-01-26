
import org.eso.ias.cdb.CdbReader;
import org.eso.ias.cdb.json.CdbJsonFiles;
import org.eso.ias.cdb.json.JsonReader;
import org.eso.ias.dasu.Dasu;
import org.eso.ias.dasu.DasuImpl;
import org.eso.ias.dasu.publisher.KafkaPublisher;
import org.eso.ias.dasu.publisher.OutputPublisher;
import org.eso.ias.dasu.subscriber.InputSubscriber;
import org.eso.ias.dasu.subscriber.KafkaSubscriber;
import org.eso.ias.prototype.input.Identifier;
import org.eso.ias.prototype.input.java.IdentifierType;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Properties;

class DasuDemo {

    public static void main(String[] args) throws IOException {

        // set log file name
        System.setProperty("log_file_name", DasuDemo.class.getSimpleName());
        Logger logger = LoggerFactory.getLogger(DasuDemo.class);

        // Build the CDB reader
        Path cdbParentPath = FileSystems.getDefault().getPath(".");
        CdbJsonFiles cdbFiles = new CdbJsonFiles(cdbParentPath);
        CdbReader cdbReader = new JsonReader(cdbFiles);

        // define the variables to process in the dasus
        String[] vars = {"Temperature", "WindSpeed"};
        // "Pressure", "WindDirection", "Humidity", "Dewpoint"};
        int[] ids = {2};

        String[] dasuIds = new String[vars.length * ids.length + 1];
        for (int i = 0; i < ids.length; i++) {
            for (int j = 0; j < vars.length; j++) {
                dasuIds[i * vars.length + j] = "Dasu" + vars[j] + ids[i];
            }
        }

        // dummy dasu
        dasuIds[dasuIds.length - 1] = "Dasudummy";

        ArrayList<Dasu> dasus = new ArrayList<>();
        Identifier supId = new Identifier("SupervisorID", IdentifierType.SUPERVISOR);

        logger.info("Creating the dasus: " + Arrays.toString(dasuIds));
        for (String id : dasuIds) {
            OutputPublisher outputPublisher = KafkaPublisher.apply(id, new Properties());
            InputSubscriber inputsProvider = new KafkaSubscriber(id, new Properties());

            // The DASU
            Identifier ident = new Identifier(id, IdentifierType.DASU, supId);
            Dasu dasu = new DasuImpl(ident, outputPublisher, inputsProvider, cdbReader, 5*1000000);
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
