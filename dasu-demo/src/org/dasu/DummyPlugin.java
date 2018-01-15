package org.dasu;


import java.util.Scanner;

import org.eso.ias.plugin.Plugin;
import org.eso.ias.plugin.PluginException;
import org.eso.ias.plugin.config.PluginConfig;
import org.eso.ias.plugin.config.Value;
import org.eso.ias.plugin.publisher.MonitorPointSender;
import org.eso.ias.plugin.publisher.PublisherException;
import org.eso.ias.plugin.publisher.impl.KafkaPublisher;
import org.eso.ias.prototype.input.java.OperationalMode;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


/**
 * publishes data from a weather station to a Kafka Queue
 */
public class DummyPlugin extends Plugin {

    /**
     * runs the plugin.
     *
     * @param args .
     */
    public static void main(String[] args) {
        logger.info("Starting dummy plugin ...");

        // name of the IASIO
        String valueId = "dummy";

        // configuration
        PluginConfig config = new PluginConfig();
        config.setId("DummyPlugin");
        config.setMonitoredSystemId("Terminal values");
        config.setSinkServer("localhost");
        config.setSinkPort(9092);

        // values
        Value dummyVal = new Value();
        dummyVal.setId(valueId);
        dummyVal.setRefreshTime(1000);
        config.setValues(new Value[]{dummyVal});

        // publisher
        KafkaPublisher publisher = new KafkaPublisher(config.getId(),
                config.getMonitoredSystemId(),
                config.getSinkServer(),
                config.getSinkPort(),
                Plugin.getScheduledExecutorService());

        // start plugin
        DummyPlugin dummy = new DummyPlugin(config, publisher);
        try {
            dummy.start();
        } catch (PublisherException pe) {
            logger.error("The plugin failed to start", pe);
            System.exit(-3);
        }

        // set mode
        dummy.setPluginOperationalMode(OperationalMode.OPERATIONAL);


        logger.info("Plugin started, waiting user input...");

        // start reading values from input
        Scanner in = new Scanner(System.in);

        while (in.hasNextDouble()) {
            double value = in.nextDouble();

            dummy.updateMonitorPointValue(valueId, value);
            logger.info("value updated to " + value);
        }

        in.close();
    }

    private static final Logger logger = LoggerFactory.getLogger(DummyPlugin.class);

    private DummyPlugin(PluginConfig config, MonitorPointSender sender) {
        super(config, sender);
    }

    /**
     * Override method to catch the exception and log a message
     * <p>
     * In the example we do not take any special action if the Plugin returns an
     * error when submitting a new value.
     */
    @Override
    public void updateMonitorPointValue(String mPointID, Object value) {
        try {
            super.updateMonitorPointValue(mPointID, value);
        } catch (PluginException pe) {
            logger.error("Error sending {} monitor point to the core of the IAS", mPointID);
        }
    }
}
